import funcs
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

#Setting Monitors
funcs.setMonitors()

colors = [["#1F1F1F", "#1F1F1F"], # panel background
          ["#6F6F6F", "#6F6F6F"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#FF0038", "#FF0038"], # border line color for current tab
          ["#4A4B4B", "#4A4B4B"],
          ["#6F6F6F","#6F6F6F"],
          ["#FF0038", "#FF0038"]]

mod = "mod4"
terminal ="urxvt"

keys = [
     Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q set Master 2dB+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -q set Master 2dB-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer -q  set Master toggle")
    ),
    Key(
        [], "XF86AudioMicMute",
        lazy.spawn("amixer -q  set Capture toggle")
    ),
   # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Goes full screen"),
    Key([mod], "period",lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma",lazy.prev_screen(),
        desc='Move focus to prev monitor'),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "123456"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),

    ])

layouts = [
    #layout.Max(),
    #layout.Stack(num_stacks=3),
    # layout.Matrix(),
     layout.MonadTall(),
     layout.MonadWide(),
     layout.RatioTile(),
    # layout.Tile(),
     layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Fira Code Nerd Font',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def genWidgetList():
    return [
   widget.Sep(
           linewidth = 0,
           padding = 6,
           foreground = colors[2],
           background = colors[0]
           ),
  widget.GroupBox(
           font = "Fira Code Nerd Font",
           fontsize = 11,
           margin_y = 3,
           margin_x = 0,
           padding_y = 5,
           padding_x = 3,
           borderwidth = 3,
           active = colors[2],
           inactive = colors[2],
           rounded = False,
           highlight_color = colors[1],
           highlight_method = "line",
           this_current_screen_border = colors[3],
           this_screen_border = colors [4],
           other_current_screen_border = colors[0],
           other_screen_border = colors[0],
           foreground = colors[2],
           background = colors[0]
           ),
  widget.Prompt(
           font = "Ubuntu Mono",
           padding = 10,
           foreground = colors[3],
           background = colors[1]
           ),
  widget.Sep(
           linewidth = 0,
           padding = 10,
           foreground = colors[2],
           background = colors[0]
           ),
widget.WindowName(
           foreground = colors[6],
           background = colors[0],
           padding = 0
           ),
 widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[0]
            ),
widget.TextBox(
            text='',
            background = colors[0],
            foreground = colors[4],
            padding=-6.5,
            fontsize=40
            ),
 widget.GenPollText( #Weather
           foreground = colors[2],
           background = colors[4],
           update_interval = 350,
           func=funcs.weather
            ),
  widget.TextBox(
            text='',
            background = colors[4],
            foreground = colors[5],
            padding=-6.5,
            fontsize=40
            ),
  widget.GenPollText( #Memory
           foreground = colors[2],
           background = colors[5],
           update_interval = 4,
           func=funcs.memory
           ),
   widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[5]
            ),
   widget.TextBox(
            text='',
            background = colors[5],
            foreground = colors[4],
            padding=-6.5,
            fontsize=40
            ),
   widget.GenPollText( #Internet
           foreground = colors[2],
           background = colors[4],
           update_interval = 2,
           func=funcs.internet,
           mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('urxvt')}
            ),
   widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[4],
            background = colors[4]
            ),
   widget.TextBox(
            text='',
            background = colors[4],
            foreground = colors[5],
            padding=-6.5,
            fontsize=40
            ),
   widget.TextBox(
            text=' ',
            background = colors[5],
            foreground = colors[2],
            fontsize=14
            ),
  widget.Volume(
           foreground = colors[2],
           background = colors[5],
           padding = 5
           ),
   widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[5]
            ),
   widget.TextBox(
            text='',
            background = colors[5],
            foreground = colors[4],
            padding=-6.5,
            fontsize=40
            ),
  widget.CurrentLayout(
           foreground = colors[2],
           background = colors[4],
           padding = 5
           ),
  widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[4],
            background = colors[4]
            ),
   widget.TextBox(
            text='',
            background = colors[4],
            foreground = colors[5],
            padding=-6.5,
            fontsize=40
            ),
  widget.Clock(
           foreground = colors[2],
           background = colors[5],
           format = "  %a, %d/%m [%H:%M]"
           ),
    widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[5]
            ),
   widget.TextBox(
            text='',
            background = colors[5],
            foreground = colors[4],
            padding=-6.5,
            fontsize=40
            ),
   widget.KeyboardLayout(
           foreground = colors[2],
           background = colors[4],
           configured_keyboards = ["pt","br"]),
   widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[4],
            background = colors[4]
            ),
   widget.TextBox(
            text='',
            background = colors[4],
            foreground = colors[5],
            padding=-6.5,
            fontsize=40
            ),
  widget.Battery(
           foreground = colors[2],
           background = colors[5],
           battery = 0,
           format = '{char} {percent:1.0%} ({hour:d}:{min:02d})',
           charge_char = " ",
           discharge_char = " "
           ),
widget.TextBox(
            text='',
            background = colors[5],
            foreground = colors[4],
            padding=-6.5,
            fontsize=40
            ),
    widget.TextBox(
            text='',
            background = colors[4],
            foreground = colors[2],
            fontsize=11,
            mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('systemctl poweroff')}
            ),
 widget.Sep(
            linewidth = 0,
            padding = 5,
            foreground = colors[2],
            background = colors[4]
            ),
 widget.Systray(
            background = colors[5]
         ),
              ]


screens = [
    Screen(
        wallpaper=funcs.wallrandom(),
        wallpaper_mode = "fill",
        top=bar.Bar(
            genWidgetList(),
            24,
        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = False
focus_on_window_activation = "smart"

wmname = "qtile"
