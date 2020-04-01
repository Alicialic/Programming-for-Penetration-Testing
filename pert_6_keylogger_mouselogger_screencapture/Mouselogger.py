import pyxhook

# fungsi ini akan dipanggil ketika data dari mouselogger perlu untuk ditampilkan atau diambil
def OnMouseEvent(event): 
    """
    Event pada mouse yang ada di pyxhook:
    + Window         : menghandle window
    + WindowName     : nama dari window
    + WindowProcName : proses backend dari window
    + Position       : 2-tuple (x,y) yang berisi koordinat dari mouse click
    + MessageName    : memunculkan pesan gerakan mouse
                       - mouse left|right|middle down <- jika mengatur MouseAllButtonsDown pada hook manager
                       - mouse right|right|middle up <- jika mengatur MouseAllButtonsUp pada hook manager
    """
    print('Window:',event.Window)
    print('Window Name:',event.WindowName)
    print('Window Proc Name:',event.WindowProcName)
    print('Position:',event.Position)
    print('Message Name:', event.MessageName)
    print('-------------------')

# membuat sebuah hook manager
hookManager = pyxhook.HookManager()

# memanggil fungsi OnMouseEvent ketika tombol pada mouse diklik
hookManager.MouseAllButtonsDown = OnMouseEvent

# memanggil fungsi OnMouseEvent ketika tombol pada mouse dilepas
hookManager.MouseAllButtonsUp = OnMouseEvent

# memanggil fungsi OnMouseEvent ketika mouse digerakkan
hookManager.MouseMovement = OnMouseEvent

# menyiapkan hook
hookManager.HookMouse()

# memulai pemantauan
hookManager.start()