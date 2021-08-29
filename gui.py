import dearpygui.dearpygui as dpg

import du

dirs = du.ducmd()

vp = dpg.create_viewport(
    title="Du Tool", width=400, height=300, x_pos=100
)

with dpg.window(
    label="My Tool", pos=(0, 0), width=400, height=300
) as window:
    pwd = du.pwdcmd()
    dpg.add_text("directory:"+str(pwd), color=(250, 250, 250, 255))
    dpg.add_text(dirs)

dpg.setup_dearpygui()
dpg.show_viewport(vp)
dpg.start_dearpygui()
