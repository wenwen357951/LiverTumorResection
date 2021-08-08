import trclab.gui.tkWindow as tkWindow
import trclab.gui.tkWindow.components as tkComponent
from trclab.gui.tkWindow.components.Properties import Properties as tkProp
from trclab.gui.tkWindow.layout.GridLayout import GridLayout as tkLayout

# HelloWorld
if __name__ == '__main__':
    button = tkComponent.Button("clickMe")
    button.set(tkProp.TEXT, "ClickMe")
    button.set(tkProp.ACTIVE_BACKGROUND_COLOR, "#fe0")
    button.set(tkProp.BACKGROUND_COLOR, "#0ef")
    button.set(tkProp.FOREGROUND_COLOR, "#fff")
    button.layout(tkLayout.COLUMN, 0)
    button.layout(tkLayout.ROW, 0)
    tkWindowBuilder = tkWindow.Builder("HelloWorld", 800, 600)
    tkWindowBuilder.append_component(button)
    tkWindowBuilder.get_components_by_internal_name('clickMe')[0].set(tkProp.WIDTH, 10)
    window = tkWindowBuilder.build()
    window.display()

    tkWindowBuilder2 = tkWindow.Builder(serialize_data=window.serialize())
    tkWindowBuilder2.set_attr(tkWindow.Attributes.TITLE, "WEE")
    tkWindowBuilder2.build().display()
