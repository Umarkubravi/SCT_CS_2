from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Strong encryption using XOR
            pixels[x, y] = (
                r ^ key,
                g ^ key,
                b ^ key
            )

    img.save(output_image)
    print("Encrypted image saved as", output_image)


def decrypt_image(input_image, output_image, key):
    # XOR decrypts using same process
    encrypt_image(input_image, output_image, key)


print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Choose option: ")

input_image = input("Enter image name: ")
key = int(input("Enter key value (0-255): "))

if choice == "1":
    encrypt_image(input_image, "encrypted.png", key)

elif choice == "2":
    decrypt_image(input_image, "decrypted.png", key)

else:
    print("Invalid choice")