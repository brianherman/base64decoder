import base64
import sys
import easygui
encoded = easygui.enterbox(title="Base64 Decoder", msg="Enter the base64 string:")
if encoded == None: sys.exit(0)
decoded = base64.b64decode(encoded.strip())
easygui.codebox(msg="Decoded string", title="Decoded", text=decoded.decode("utf8"))