document.addEventListener("DOMContentLoaded", function () {
  // Elementos do formulário
  const form = document.getElementById("serviceForm");
  const customerTypeRadios = document.querySelectorAll(
    'input[name="customerType"]'
  );
  const existingCustomerSection = document.getElementById(
    "existingCustomerSection"
  );
  const newCustomerSection = document.getElementById("newCustomerSection");
  const assignDriverCheckbox = document.getElementById("assignDriver");
  const driverSection = document.getElementById("driverSection");
  const sameAddressCheckbox = document.getElementById("sameAddress");
  const customerAddressSection = document.getElementById(
    "customerAddressSection"
  );
  const geocodeBtn = document.getElementById("btnGeocode");
  const addressInput = document.getElementById("address");
  const latitudeDisplay = document.getElementById("latitudeDisplay");
  const longitudeDisplay = document.getElementById("longitudeDisplay");
  const latitudeSpan = document.getElementById("latitude");
  const longitudeSpan = document.getElementById("longitude");
  const useCustomerAddressCheckbox =
    document.getElementById("useCustomerAddress");

  const selectedType = document.querySelector(
    'input[name="customerType"]:checked'
  );
  if (selectedType && selectedType.value === "existing") {
    useCustomerAddressCheckbox.parentElement.style.display = "block";
  }

  // Inicialização
  loadCustomers();
  useCustomerAddressCheckbox.parentElement.style.display = "none";

  // Botão de recarregar clientes
  const reloadBtn = document.getElementById("reloadCustomers");
  if (reloadBtn) {
    reloadBtn.addEventListener("click", loadCustomers);
  }

  // Alternância entre cliente existente e novo
  customerTypeRadios.forEach((radio) => {
    radio.addEventListener("change", function () {
      if (this.value === "existing") {
        existingCustomerSection.style.display = "block";
        newCustomerSection.style.display = "none";
        useCustomerAddressCheckbox.parentElement.style.display = "block";
      } else {
        existingCustomerSection.style.display = "none";
        newCustomerSection.style.display = "block";
        useCustomerAddressCheckbox.checked = false;
        useCustomerAddressCheckbox.parentElement.style.display = "none";
        addressInput.disabled = false;
        geocodeBtn.disabled = false;
      }
    });
  });

  // Usar endereço do cliente existente
  useCustomerAddressCheckbox.addEventListener("change", function () {
    if (this.checked) {
      addressInput.disabled = true;
      geocodeBtn.disabled = true;
      latitudeSpan.textContent = "";
      longitudeSpan.textContent = "";
      latitudeDisplay.style.display = "none";
      longitudeDisplay.style.display = "none";
    } else {
      addressInput.disabled = false;
      geocodeBtn.disabled = false;
    }
  });

  // Mostrar/ocultar seção de motorista
  assignDriverCheckbox.addEventListener("change", function () {
    driverSection.style.display = this.checked ? "block" : "none";
    if (this.checked) loadDrivers();
  });

  // Usar mesmo endereço do serviço
  sameAddressCheckbox.addEventListener("change", function () {
    if (this.checked) {
      document.getElementById("customerAddress").value = addressInput.value;
      customerAddressSection.style.display = "none";
    } else {
      customerAddressSection.style.display = "block";
    }
  });

  // Geocodificar endereço
  geocodeBtn.addEventListener("click", async function () {
    const address = addressInput.value;
    if (!address) {
      alert("Por favor, insira um endereço para geocodificar.");
      return;
    }

    try {
      const encodedAddress = encodeURIComponent(address);
      const response = await fetch(`/api/geocode/${encodedAddress}`);
      if (!response.ok) throw new Error("Erro ao geocodificar endereço");
      const data = await response.json();
      if (data && data.latitude && data.longitude) {
        latitudeSpan.textContent = data.latitude;
        longitudeSpan.textContent = data.longitude;
        latitudeDisplay.style.display = "inline";
        longitudeDisplay.style.display = "inline";
      } else {
        alert("Não foi possível obter as coordenadas para este endereço.");
      }
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao geocodificar endereço: " + error.message);
    }
  });

  // Envio do formulário
  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    const useExistingAddress = useCustomerAddressCheckbox.checked;
    const isExistingCustomer =
      document.querySelector('input[name="customerType"]:checked').value ===
      "existing";

    if (
      !useExistingAddress &&
      (!latitudeSpan.textContent || !longitudeSpan.textContent)
    ) {
      alert(
        "Por favor, geocodifique o endereço ou marque 'Usar endereço do cliente'."
      );
      return;
    }

    const serviceData = {
      code: document.getElementById("code").value,
      title: document.getElementById("title").value,
      note: document.getElementById("note").value,
      type: document.getElementById("type").value,
      upsert: true,
      ...(isExistingCustomer && useExistingAddress
        ? {}
        : {
            address: addressInput.value,
            latitude: parseFloat(latitudeSpan.textContent),
            longitude: parseFloat(longitudeSpan.textContent),
          }),
    };

    // Cliente
    if (isExistingCustomer) {
      const customerId = document.getElementById("customerId").value;
      if (customerId) serviceData.customer_id = customerId;
    } else {
      serviceData.customer = {
        name: document.getElementById("customerName").value,
        email: document.getElementById("customerEmail").value,
        phone_number: document.getElementById("customerPhone").value,
        address: sameAddressCheckbox.checked
          ? addressInput.value
          : document.getElementById("customerAddress").value,
        upsert: true,
      };
      const complement = document.getElementById("addressComplement").value;
      if (complement) serviceData.customer.address_complement = complement;
    }

    // Motorista
    if (assignDriverCheckbox.checked) {
      const driverId = document.getElementById("driverId").value;
      if (driverId) serviceData.driver_id = driverId;
    }

    try {
      const response = await fetch("/api/services", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(serviceData),
      });

      const result = await response.json();
      const resultModalBody = document.getElementById("resultModalBody");

      if (response.ok) {
        resultModalBody.innerHTML = `
          <div class="alert alert-success">Serviço cadastrado com sucesso!</div>
          <pre>${JSON.stringify(result, null, 2)}</pre>
          <div class="text-end mt-3">
            <button id="btnNovoServico" class="btn btn-primary">Novo Serviço</button>
          </div>
        `;

        // Botão "Novo Serviço"
        setTimeout(() => {
          document
            .getElementById("btnNovoServico")
            .addEventListener("click", () => {
              bootstrap.Modal.getInstance(
                document.getElementById("resultModal")
              ).hide();
              form.reset();
              latitudeSpan.textContent = "";
              longitudeSpan.textContent = "";
              latitudeDisplay.style.display = "none";
              longitudeDisplay.style.display = "none";
              existingCustomerSection.style.display = "block";
              newCustomerSection.style.display = "none";
              driverSection.style.display = "none";
              customerAddressSection.style.display = "block";
              useCustomerAddressCheckbox.checked = false;
              useCustomerAddressCheckbox.parentElement.style.display = "block";
              addressInput.disabled = false;
              geocodeBtn.disabled = false;
              document.getElementById("code").focus();
            });
        }, 50);
      } else {
        resultModalBody.innerHTML = `
          <div class="alert alert-danger">Erro ao cadastrar serviço</div>
          <pre>${JSON.stringify(result, null, 2)}</pre>
        `;
      }

      new bootstrap.Modal(document.getElementById("resultModal")).show();
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao enviar formulário: " + error.message);
    }
  });

  // Carregar clientes
  async function loadCustomers() {
    try {
      const response = await fetch("/api/contatos");
      if (!response.ok) throw new Error("Erro ao buscar clientes");
      const data = await response.json();
      const customerSelect = document.getElementById("customerId");
      customerSelect.innerHTML = "";
      const customers = Array.isArray(data) ? data : data.data || [];
      if (customers.length) {
        customers.forEach((c) => {
          const option = document.createElement("option");
          option.value = c.id || c.code;
          option.textContent = `${c.code || c.id} - ${c.name} - ${
            c.address || "Sem endereço"
          }`;
          customerSelect.appendChild(option);
        });
      } else {
        customerSelect.innerHTML =
          '<option value="">Nenhum cliente encontrado</option>';
      }
    } catch (error) {
      console.error("Erro ao carregar clientes:", error);
    }
  }

  // Carregar motoristas
  async function loadDrivers() {
    try {
      const response = await fetch("/api/drivers");
      if (!response.ok) throw new Error("Erro ao buscar motoristas");
      const data = await response.json();
      const driverSelect = document.getElementById("driverId");
      driverSelect.innerHTML = "";
      const drivers = Array.isArray(data) ? data : data.data || [];
      if (drivers.length) {
        drivers.forEach((d) => {
          const option = document.createElement("option");
          option.value = d.id || d.code;
          option.textContent = `${d.code || d.id} - ${d.name}`;
          driverSelect.appendChild(option);
        });
      } else {
        driverSelect.innerHTML =
          '<option value="">Nenhum motorista encontrado</option>';
      }
    } catch (error) {
      console.error("Erro ao carregar motoristas:", error);
    }
  }
});
