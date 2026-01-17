import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap
import io

st.set_page_config(page_title="Text to Screenshot", layout="centered")

st.title("📝 Text → Paragraph Screenshot (Safe)")
st.write("Enter anything. It will show as a paragraph and can be downloaded as an image.")

# Input
text = st.text_area("Enter your text 👇", height=200)

# Show paragraph output
if text:
    st.subheader("📄 Output (Paragraph View)")
    st.write(text)

    # Create image from text
    img_width = 800
    padding = 40
    font_size = 20

    try:
        font = ImageFont.truetype("DejaVuSans.ttf", font_size)
    except:
        font = ImageFont.load_default()

    wrapped_text = textwrap.fill(text, width=70)
    lines = wrapped_text.split("\n")
    img_height = padding * 2 + len(lines) * (font_size + 10)

    img = Image.new("RGB", (img_width, img_height), "white")
    draw = ImageDraw.Draw(img)

    y = padding
    for line in lines:
        draw.text((padding, y), line, fill="black", font=font)
        y += font_size + 10

    # Convert image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    st.subheader("📸 Download Screenshot")
    st.download_button(
        label="Download as Image",
        data=img_bytes,
        file_name="text_screenshot.png",
        mime="image/png"
    )
