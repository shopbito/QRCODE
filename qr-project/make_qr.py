import qrcode
from PIL import Image
import os

# ========== تنظیمات شما ==========
URL = "https://mohammadalikalbasi.ir"
OUTPUT_FOLDER = "output"
LOGO_FILE = None  # اگه لوگو داری، اسم فایل رو اینجا بنویس مثلاً: "logo.png"
# =================================

# ساخت پوشه خروجی
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ۱. QR ساده
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(os.path.join(OUTPUT_FOLDER, "qr-basic.png"))
print("✅ QR ساده ساخته شد")

# ۲. QR رنگی
img_color = qr.make_image(fill_color="#1a1a2e", back_color="#f5f5f5")
img_color.save(os.path.join(OUTPUT_FOLDER, "qr-colored.png"))
print("✅ QR رنگی ساخته شد")

# ۳. QR با لوگو (اگه لوگو داری)
if LOGO_FILE and os.path.exists(LOGO_FILE):
    qr_big = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr_big.add_data(URL)
    qr_big.make(fit=True)
    
    img_qr = qr_big.make_image(fill_color="#1a1a2e", back_color="white").convert("RGBA")
    
    logo = Image.open(LOGO_FILE).convert("RGBA")
    qr_width, qr_height = img_qr.size
    logo_size = qr_width // 4
    logo.thumbnail((logo_size, logo_size), Image.LANCZOS)
    
    pos = ((qr_width - logo.size[0]) // 2, (qr_height - logo.size[1]) // 2)
    img_qr.paste(logo, pos, logo)
    img_qr.save(os.path.join(OUTPUT_FOLDER, "qr-with-logo.png"))
    print("✅ QR با لوگو ساخته شد")

print(f"\n🎉 همه فایل‌ها در پوشه '{OUTPUT_FOLDER}' ذخیره شدند!")