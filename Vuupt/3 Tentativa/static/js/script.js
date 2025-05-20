// static/js/script.js
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

  // Elementos para geocodificação
  const addressInput = document.getElementById("address");
  const latitudeDisplay = document.getElementById("latitudeDisplay");
  const longitudeDisplay = document.getElementById("longitudeDisplay");
  const latitudeSpan = document.getElementById("latitude");
  const longitudeSpan = document.getElementById("longitude");

  // Carregar clientes ao iniciar
  loadCustomers();

  //Botão de recarregar clientes
  const reloadBtn = document.getElementById("reloadCustomers");
  reloadBtn.addEventListener("click", function () {
    loadCustomers();
  });

  // Eventos para alternar entre cliente existente e novo cliente
  customerTypeRadios.forEach((radio) => {
    radio.addEventListener("change", function () {
      if (this.value === "existing") {
        existingCustomerSection.style.display = "block";
        newCustomerSection.style.display = "none";
      } else {
        existingCustomerSection.style.display = "none";
        newCustomerSection.style.display = "block";
      }
    });
  });

  // Evento para mostrar/ocultar seção de motorista
  assignDriverCheckbox.addEventListener("change", function () {
    if (this.checked) {
      driverSection.style.display = "block";
      loadDrivers();
    } else {
      driverSection.style.display = "none";
    }
  });

  // Evento para usar o mesmo endereço do serviço
  sameAddressCheckbox.addEventListener("change", function () {
    if (this.checked) {
      document.getElementById("customerAddress").value = addressInput.value;
      customerAddressSection.style.display = "none";
    } else {
      customerAddressSection.style.display = "block";
    }
  });

  // Evento para geocodificar endereço
  geocodeBtn.addEventListener("click", async function () {
    const address = addressInput.value;
    if (!address) {
      alert("Por favor, insira um endereço para geocodificar.");
      return;
    }

    try {
      const encodedAddress = encodeURIComponent(address);
      const response = await fetch(`/api/geocode/${encodedAddress}`);
      if (!response.ok) {
        throw new Error("Erro ao geocodificar endereço");
      }

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

  // Evento para o envio do formulário
  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    // Validar se o endereço foi geocodificado
    if (!latitudeSpan.textContent || !longitudeSpan.textContent) {
      alert("Por favor, geocodifique o endereço antes de enviar.");
      return;
    }

    // Preparar os dados do serviço
    const serviceData = {
      code: document.getElementById("code").value,
      title: document.getElementById("title").value,
      note: document.getElementById("note").value,
      type: document.getElementById("type").value,
      address: addressInput.value,
      latitude: parseFloat(latitudeSpan.textContent),
      longitude: parseFloat(longitudeSpan.textContent),
      upsert: true,
    };

    // Verificar tipo de cliente (existente ou novo)
    const customerType = document.querySelector(
      'input[name="customerType"]:checked'
    ).value;
    if (customerType === "existing") {
      const customerId = document.getElementById("customerId").value;
      if (customerId) {
        serviceData.customer_id = customerId;
      }
    } else {
      // Cliente novo
      serviceData.customer = {
        name: document.getElementById("customerName").value,
        email: document.getElementById("customerEmail").value,
        phone_number: document.getElementById("customerPhone").value,
        upsert: true,
      };

      // Verificar se usa o mesmo endereço ou um endereço próprio
      if (sameAddressCheckbox.checked) {
        serviceData.customer.address = addressInput.value;
      } else {
        serviceData.customer.address =
          document.getElementById("customerAddress").value;
      }

      // Adicionar complemento se existir
      const complement = document.getElementById("addressComplement").value;
      if (complement) {
        serviceData.customer.address_complement = complement;
      }
    }

    // Verificar se deve atribuir a um motorista
    if (assignDriverCheckbox.checked) {
      const driverId = document.getElementById("driverId").value;
      if (driverId) {
        serviceData.driver_id = driverId;
      }
    }

    try {
      const response = await fetch("/api/services", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(serviceData),
      });

      const result = await response.json();

      // Mostrar resultado em um modal
      const resultModalBody = document.getElementById("resultModalBody");
      if (response.ok) {
        resultModalBody.innerHTML = `
  <div class="alert alert-success">Serviço cadastrado com sucesso!</div>
  <pre>${JSON.stringify(result, null, 2)}</pre>
  <div class="text-end mt-3">
    <button id="btnNovoServico" class="btn btn-primary">Novo Serviço</button>
  </div>
`;

        // Adiciona o event listener assim que o botão for inserido no DOM
        document
          .getElementById("btnNovoServico")
          .addEventListener("click", () => {
            // Fechar o modal
            const modalElement = document.getElementById("resultModal");
            const modalInstance = bootstrap.Modal.getInstance(modalElement);
            modalInstance.hide();

            // Limpar os campos do formulário
            form.reset();

            // Resetar campos de latitude e longitude
            latitudeSpan.textContent = "";
            longitudeSpan.textContent = "";
            latitudeDisplay.style.display = "none";
            longitudeDisplay.style.display = "none";

            // Reexibir seção correta do cliente
            existingCustomerSection.style.display = "block";
            newCustomerSection.style.display = "none";

            // Ocultar seção de motorista e endereço adicional
            driverSection.style.display = "none";
            customerAddressSection.style.display = "block";

            // Restaurar foco no campo de código
            document.getElementById("code").focus();
          });
      } else {
        resultModalBody.innerHTML = `
                    <div class="alert alert-danger">Erro ao cadastrar serviço</div>
                    <pre>${JSON.stringify(result, null, 2)}</pre>
                `;
      }

      // Exibir o modal
      new bootstrap.Modal(document.getElementById("resultModal")).show();
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao enviar formulário: " + error.message);
    }
  });

  // Função para carregar clientes
  async function loadCustomers() {
    try {
      // Usa a rota do backend que fará a proxy para a API externa
      const response = await fetch("/api/contatos");
      if (!response.ok) {
        throw new Error("Erro ao buscar clientes");
      }

      const data = await response.json();
      const customerSelect = document.getElementById("customerId");
      customerSelect.innerHTML = ""; // Limpar opções existentes

      // Verifica se a resposta é um array ou tem uma propriedade data
      const customers = Array.isArray(data) ? data : data.data || [];

      if (customers && customers.length > 0) {
        customers.forEach((customer) => {
          const option = document.createElement("option");
          option.value = customer.id || customer.code;
          option.textContent = `${customer.id || customer.code} - ${
            customer.name
          }- ${customer.address || "Sem endereço"}`;
          customerSelect.appendChild(option);
        });
      } else {
        const option = document.createElement("option");
        option.value = "";
        option.textContent = "Nenhum cliente encontrado";
        customerSelect.appendChild(option);
      }
    } catch (error) {
      console.error("Erro ao carregar clientes:", error);
      const customerSelect = document.getElementById("customerId");
      customerSelect.innerHTML =
        '<option value="">Erro ao carregar clientes</option>';
    }
  }

  // Função para carregar motoristas
  async function loadDrivers() {
    try {
      // Usa a rota do backend que fará a proxy para a API externa
      const response = await fetch("/api/drivers");
      if (!response.ok) {
        throw new Error("Erro ao buscar motoristas");
      }

      const data = await response.json();
      const driverSelect = document.getElementById("driverId");
      driverSelect.innerHTML = ""; // Limpar opções existentes

      //Botão de recarregar motoristas
      const reloadBtn = document.getElementById("reloadDrivers");
      reloadBtn.addEventListener("click", function () {
        loadDrivers();
      });

      // Verifica se a resposta é um array ou tem uma propriedade data
      const drivers = Array.isArray(data) ? data : data.data || [];

      if (drivers && drivers.length > 0) {
        drivers.forEach((driver) => {
          const option = document.createElement("option");
          option.value = driver.id || driver.code; // Alguns APIs usam code em vez de id
          option.textContent = `${driver.id || driver.code} - ${driver.name}`;
          driverSelect.appendChild(option);
        });
      } else {
        const option = document.createElement("option");
        option.value = "";
        option.textContent = "Nenhum motorista encontrado";
        driverSelect.appendChild(option);
      }
    } catch (error) {
      console.error("Erro ao carregar motoristas:", error);
      const driverSelect = document.getElementById("driverId");
      driverSelect.innerHTML =
        '<option value="">Erro ao carregar motoristas</option>';
    }
  }
});
