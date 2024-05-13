import qrcode
import ttkbootstrap as ttk
from tkinter import *

app = ttk.Window(
    title="QR Generator",
    themename="vapor",
    resizable=(False, False),
)
app.geometry('600x600')


def generate_qr_code():
    text = text_entry.get()
    file_name = "QR.png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
        image_factory=None,
        mask_pattern=None,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(back_color="#435E55FF", fill_color="#D64161FF")
    img.save(file_name)
    demo_media = PhotoImage(file="QR.png")
    label.configure(image=demo_media)
    label.image = demo_media
    label.place(x=150, y=200)
    label.pack(expand=False)
    return


label = ttk.Label(app, text="QR Generator", bootstyle="secondary")
label.pack(pady=30)
label.config(font=('Consolas', 15))

text_frame = ttk.Frame(app)
text_frame.pack(pady=15, padx=10, fill='x')
ttk.Label(text_frame, text='Enter text:').pack(side="left")

text_entry = ttk.Entry(text_frame, validate="focus")
text_entry.pack(side='left', fill="x", expand=True, padx=5)

demo_media = ttk.PhotoImage(file="")
label = ttk.Label(app, image=demo_media)
label.place(x=150, y=200)
label.pack(expand=False)

button = ttk.Button(text_frame, text="Generate", bootstyle="secondary", command=generate_qr_code)
button.pack(pady=10)

app.mainloop()
