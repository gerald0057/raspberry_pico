from machine import SPI

# spi = SPI(0)
spi = SPI(0, 100_000)
# spi = SPI(0, 100_000, polarity=1, phase=1)

print(spi.write('test'))
print(spi.read(5))

buf = bytearray(3)
spi.write_readinto('out', buf)
print(buf)