import sublime
import sublime_plugin


class HexBinSwapperCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 20
    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
        for j in range(0, len(reglist)):
            sel_text = v.substr(v.sel()[j])
            if sel_text.startswith("0b") or sel_text.startswith("0B") :
                sel_text = sel_text.strip().lstrip("0b").lstrip("0B").replace(" ","")
                l = True
                if sel_text == '':
                    l = False
                for i in sel_text:
                    if not((i == '1') or (i == '0')):
                        l = False
                if l:
                    v.replace(edit, v.sel()[j], '0x{0:X}'.format(int(sel_text, 2)))
                else:
                    if len(sel_text) > self.MAX_STR_LEN:
                        logMsg = sel_text[0:self.MAX_STR_LEN] + "..."
                    else:
                        logMsg = sel_text
                    sublime.status_message("\"%s\" isn't a binary number!" % logMsg)
                    sublime.error_message("\"%s\" isn't a binary number!" % logMsg)
            elif sel_text.startswith("0x") or sel_text.startswith("0X"):
                sel_text = v.substr(v.sel()[j])
                sel_text = sel_text.strip().lstrip("0x").lstrip("0X")
                # print(sel_text)
                hexdig = '0123456789abcdefABCDEF'
                l = True
                if sel_text == '':
                    l = False
                for i in sel_text:
                    if not(i in hexdig):
                        l = False

                if l:
                    v.replace(edit, v.sel()[j], '0b{0:0>8b}'.format(int(sel_text, 16)))
                else:
                    if len(sel_text) > self.MAX_STR_LEN:
                        logMsg = sel_text[0:self.MAX_STR_LEN] + "..."
                    else:
                        logMsg = sel_text
                    sublime.status_message("\"%s\" isn't a hexadecimal number!" % logMsg)
                    sublime.error_message("\"%s\" isn't a hexadecimal number!" % logMsg)
            else:
                if len(sel_text) > self.MAX_STR_LEN:
                    logMsg = sel_text[0:self.MAX_STR_LEN] + "..."
                else:
                    logMsg = sel_text
                sublime.status_message("\"%s\" isn't a hex or bin number!" % logMsg)
                sublime.error_message("\"%s\" isn't a hex or bin number!" % logMsg)


