import os
import qrcode

def generate_qr_code(url, folder = "output", filename = "qrcode.png"):
    # Get the script's directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Combine the script's directory with the specified folder
    output_folder = os.path.join(script_directory, folder)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Create QR code instance
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit = True)

    # Create an image from the QR code data
    color_mode = input("If you want default colors , white and black then enter 'D' , else enter 'C' to customize : ")
    color_mode = color_mode.upper()
    if color_mode == 'D':
        img = qr.make_image(fill_color="black", back_color="white")
    elif color_mode == 'C':
        fill_col = input('Enter the fill color : ')
        back_col = input('Enter the  background color : ')
        img = qr.make_image(fill_color=fill_col, back_color=back_col)
    

    # Save the image in the specified folder
    file_path = os.path.join(output_folder, filename)
    img.save(file_path)

    print("QR code generated and saved as qrcode.png")

if __name__ == "__main__":
    # Prompt the user to enter the URL
    url_to_encode = input("Enter the URL for QR code generation: ")

    # Call the function to generate QR code and save it in the "output" folder
    generate_qr_code(url_to_encode)
