movieName = "The Godfather"
movieDescription = """The Godfather
is a 1972 American crime film"""
print(movieName.upper()) # THE GODFATHER
print(movieName.lower()) # the godfather
print(movieName.capitalize()) # The godfather
print(movieDescription.title()) # The Godfather
print(movieDescription.swapcase()) # tHE gODFATHER
print(movieDescription.replace("The", "A")) # A Godfather
print(movieName.center(30, "-")) # -------The Godfather--------