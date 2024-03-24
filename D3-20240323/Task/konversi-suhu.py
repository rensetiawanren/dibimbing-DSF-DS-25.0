def celcius_ke_fahrenheit(celcius):
  """
  Mengkonversi suhu dari Celcius ke Fahrenheit.

  Args:
    celcius: Suhu dalam Celcius (float).

  Returns:
    Suhu dalam Fahrenheit (float).
  """

  fahrenheit = (celcius * 9/5) + 32
  return fahrenheit

# Input suhu Celcius
celcius = float(input("Masukkan suhu Celcius: "))

# Konversi Celcius ke Fahrenheit
fahrenheit = celcius_ke_fahrenheit(celcius)

# Print hasil konversi
print(f"{celcius} derajat Celcius sama dengan {fahrenheit} derajat Fahrenheit.")