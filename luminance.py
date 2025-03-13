BUFFER_SIZE = 256 

def process_rgb_to_gray(hex_input: str, width: int, height: int) -> list[int]:
    

    str_len = len(hex_input)

    if str_len % 2 != 0:
        raise ValueError("Hex string length must be even.")
    
    bytes_len = str_len // 2
    if bytes_len > BUFFER_SIZE:
        raise ValueError(f"Byte length ({bytes_len}) exceeds buffer size {BUFFER_SIZE}.")
  
    shared_buffer = [0] * bytes_len
    for i in range(bytes_len):
        high_char = hex_input[2*i]
        low_char  = hex_input[2*i + 1]
        high_val = hex_to_int(high_char)
        low_val  = hex_to_int(low_char)
        if high_val < 0 or low_val < 0:
            raise ValueError(f"Invalid hex character '{high_char}{low_char}' at position {2*i}.")
        shared_buffer[i] = (high_val << 4) | low_val

    pixel_count = width * height
    if bytes_len < pixel_count * 3:
        raise ValueError("Hex data is not enough to cover all pixels (width*height*3).")

    grayscale = [0] * pixel_count
    for i in range(pixel_count):
        r = shared_buffer[i*3]
        g = shared_buffer[i*3 + 1]
        b = shared_buffer[i*3 + 2]
        gray_val = (r * 77 + g * 150 + b * 29) >> 8
        grayscale[i] = gray_val
    
    return grayscale


def apply_brightness(grayscale: list[int], brightness_offset: int) -> None:
    for i in range(len(grayscale)):
        val = grayscale[i] + brightness_offset
        if val < 0:
            val = 0
        elif val > 255:
            val = 255
        grayscale[i] = val


def hex_to_int(c: str) -> int:
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    if 'A' <= c <= 'F':
        return ord(c) - ord('A') + 10
    if 'a' <= c <= 'f':
        return ord(c) - ord('a') + 10
    return -1


def main():
    test_image_hex = (
        "47704C47704C47704C000000FFFFFF04040347704C47704C"
        "47704C95BF2BA9CB431467AB145194EFEFEF47704C47704C"
        "47704C9AC32DFFFFFF135EA4145194123C73A0BBCD47704C"
        "000000FFFFFF49AEDA8DD3F05E7C94265B94FFFFFF040503"
        "000000FFFFFFFEE404E3D236363531979255485F13000000"
        "47704CFFFFFFFEF02FF6F6F6E6EBF6E6EBF65F861C47704C"
        "47704C47704CE1E1E1F4F4F4F6F6F678A023FEFEFE47704C"
        "47704C47704C89B13B00000000000047704C47704CFFFFFF"
    )
    width = 8
    height = 8

    print("Testing grayscale in Python with 8x8 sample image...")

    try:
        gray_output = process_rgb_to_gray(test_image_hex, width, height)
        print("process_rgb_to_gray success!")
        print(f"Total pixels: {len(gray_output)}")
        
        print("First pixel (grayscale):", gray_output[0])
        print("Last  pixel (grayscale):", gray_output[-1])

        apply_brightness(gray_output, 50)
        print("After brightness +50 on first pixel:", gray_output[0])

    except ValueError as e:
        print(f"Error occurred: {e}")



if __name__ == "__main__":
    main()
