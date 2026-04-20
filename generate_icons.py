from PIL import Image
import os

src = r"D:\Personal\Desktop\111\111.png"
base = r"D:\Personal\Desktop\luoda-rustdesk"

img = Image.open(src).convert("RGBA")
print(f"Source: {img.size}")

def save_png(path, size):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    resized = img.resize((size, size), Image.Resampling.LANCZOS)
    resized.save(path, "PNG")
    print(f"Saved: {path} ({size}x{size})")

def save_ico(path, sizes):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    imgs = [img.resize((s, s), Image.Resampling.LANCZOS) for s in sizes]
    imgs[0].save(path, "ICO", sizes=[(s, s) for s in sizes])
    print(f"Saved ICO: {path} {sizes}")

# Windows exe icon
save_ico(os.path.join(base, "flutter", "windows", "runner", "resources", "app_icon.ico"), [16, 32, 48, 256])

# Windows MSI icon
save_ico(os.path.join(base, "res", "icon.ico"), [16, 32, 48, 256])

# Tray icon
save_ico(os.path.join(base, "res", "tray-icon.ico"), [16, 32, 48])

# Android mipmap icons
android_sizes = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
android_base = os.path.join(base, "flutter", "android", "app", "src", "main", "res")
for density, size in android_sizes.items():
    save_png(os.path.join(android_base, f"mipmap-{density}", "ic_launcher.png"), size)
    save_png(os.path.join(android_base, f"mipmap-{density}", "ic_launcher_round.png"), size)
    save_png(os.path.join(android_base, f"mipmap-{density}", "ic_stat_logo.png"), size)

# Android foreground (adaptive icon)
save_png(os.path.join(android_base, "mipmap-mdpi", "ic_launcher_foreground.png"), 108)
save_png(os.path.join(android_base, "mipmap-hdpi", "ic_launcher_foreground.png"), 162)
save_png(os.path.join(android_base, "mipmap-xhdpi", "ic_launcher_foreground.png"), 216)
save_png(os.path.join(android_base, "mipmap-xxhdpi", "ic_launcher_foreground.png"), 324)
save_png(os.path.join(android_base, "mipmap-xxxhdpi", "ic_launcher_foreground.png"), 432)

# Flutter assets
save_png(os.path.join(base, "flutter", "assets", "icon.png"), 512)

# res folder icons (various sizes)
for size in [16, 32, 48, 64, 128, 256]:
    save_png(os.path.join(base, "res", f"icon-{size}.png"), size)
save_png(os.path.join(base, "res", "icon.png"), 512)
save_png(os.path.join(base, "res", "128x128.png"), 128)
save_png(os.path.join(base, "res", "128x128@2x.png"), 256)
save_png(os.path.join(base, "res", "32x32.png"), 32)
save_png(os.path.join(base, "res", "64x64.png"), 64)

# iOS icons (1024x1024 base, will resize)
ios_sizes = [20, 29, 40, 60, 76, 83.5]
for size in [20, 29, 40, 60, 76, 83, 1024]:
    for scale in [1, 2, 3]:
        final_size = size * scale
        folder = os.path.join(base, "flutter", "ios", "Runner", "Assets.xcassets", "AppIcon.appiconset")
        save_png(os.path.join(folder, f"Icon-App-{size}x{size}@{scale}x.png"), final_size)

# macOS AppIcon.icns (PNG components for now)
macos_folder = os.path.join(base, "flutter", "macos", "Runner")
for size in [16, 32, 64, 128, 256, 512, 1024]:
    save_png(os.path.join(macos_folder, f"app_icon_{size}.png"), size)

# Also create icns placeholder (just PNG for now, real icns needs extra tools)
# Just copy 512 and 1024 as placeholders
img.resize((512, 512), Image.Resampling.LANCZOS).save(os.path.join(macos_folder, "AppIcon.icns"), format="PNG")
print(f"Note: macOS icns is placeholder - needs iconutil on macOS")

print("\n✅ All icons generated!")