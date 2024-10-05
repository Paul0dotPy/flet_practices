# App responsive para la versión de Flet 0.23.2

from flet import app, Page, ThemeMode, ResponsiveRow, Container, Row, Column, NavigationRail, NavigationRailDestination, icons, alignment, MainAxisAlignment, IconButton, Switch, padding, Text, TextField, Row, InputBorder, Dropdown, dropdown, Theme, ControlState, TextStyle

class UI(ResponsiveRow):
    def __init__(self, page):
        super().__init__()
        self.color_teal = "teal"
        self.page = page
        self.expand = True

        self.mode_switch = Switch(
            value=True,
            on_change=self.mode_theme,
            thumb_color="black",
            thumb_icon={
                ControlState.DEFAULT: icons.LIGHT_MODE,
                ControlState.SELECTED: icons.DARK_MODE
            }
        )

        self.init_container_1 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Día"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.init_container_2 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Semana"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.loc_container_1 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Ubicación-Día"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.loc_container_2 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Ubicación-Semana"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.cal_container_1 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Calendario-Día"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.cal_container_2 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Calendario-Semana"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.conf_container_1 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Configuración-Día"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.conf_container_2 = Container(
            bgcolor=self.color_teal,
            border_radius=20,
            padding=20,
            content=Column(
                controls=[
                    Text("Configuración-Semana"),
                    Container(
                        border_radius=20
                    )
                ]
            )
        )

        self.container_list_1 = [self.init_container_1, self.loc_container_1, self.cal_container_1, self.conf_container_1]
        self.container_list_2 = [self.init_container_2, self.loc_container_2, self.cal_container_2, self.conf_container_2]
        self.container_1 = Container(content=self.container_list_1[0], expand=True)
        self.container_2 = Container(content=self.container_list_2[0], expand=True)

        self.nav_container = Container(
            col={"sm":2, "md":1.5, "lg":1},
            border_radius=10,
            bgcolor=self.color_teal,
            content=Column(
                controls=[
                    Container(
                        alignment=alignment.center,
                        expand=True,
                        content=NavigationRail(
                            bgcolor=self.color_teal,
                            #expand=True,
                            on_change=self.switch_page,
                            #extended=True,
                            selected_index=0,
                            elevation=10,
                            #group_alignment=0.9,
                            destinations=[
                                NavigationRailDestination(
                                    icon=icons.HOME,
                                    label="Inicio"
                                ),
                                NavigationRailDestination(
                                    icon=icons.LOCATION_ON_OUTLINED,
                                    label="Loc"
                                ),
                                NavigationRailDestination(
                                    icon=icons.CALENDAR_MONTH_SHARP,
                                    label="Fecha"
                                ),
                                NavigationRailDestination(
                                    icon=icons.SETTINGS,
                                    label_content=Text("Conf", size=10.5)
                                )
                            ]
                        )
                    ),
                    Container(
                        expand=True,
                        alignment=alignment.center,
                        content=Column(
                            alignment=MainAxisAlignment.END,                            
                            controls=[
                                Row([IconButton(icon=icons.OUTPUT)], alignment=MainAxisAlignment.CENTER),
                                Row([self.mode_switch], alignment=MainAxisAlignment.CENTER)
                            ]
                        )
                    )
                ]
            )
        )

        self.frame_2 = Container(
            col={"sm":5, "md": 5.5, "lg":6},
            content=Column(
                controls=[
                    ResponsiveRow(
                        controls=[
                            Container(
                                border_radius=10,
                                alignment=alignment.top_left,
                                col={"sm":10, "md":9, "lg":8},
                                content=Container(
                                    bgcolor=self.color_teal,
                                    border_radius=20,
                                    content=Row(
                                        controls=[
                                            IconButton(icon=icons.SEARCH),
                                            TextField(hint_text="Buscar ciudad",
                                                      border=InputBorder.NONE,
                                                      border_radius=20)
                                        ]
                                    )
                                )
                            )
                        ]
                    ),
                    self.container_1,
                    self.container_2
                ]
            )
        )

        self.frame_3 = Container(
            col=5,
            content=Column(
                controls=[
                    ResponsiveRow(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            Container(
                                alignment=alignment.center_right,
                                col={"sm":9, "md":6, "lg":6},
                                content=Container(
                                    bgcolor=self.color_teal,
                                    padding=5,
                                    border_radius=20,
                                    content=Dropdown(
                                        border_color="transparent",
                                        border_radius=20,
                                        hint_text="Inicio",
                                        options=[
                                            dropdown.Option("Inicio"),
                                            dropdown.Option("Configuracion"),
                                            dropdown.Option("Salir")
                                        ]
                                    )
                                )
                            )
                        ]
                    ),
                    Container(
                        border_radius=20,
                        #padding=5,
                        expand=True,
                        content=Column(
                            controls=[
                                Container(
                                    content=Text("Aspectos destacados de hoy")
                                ),
                                ResponsiveRow(
                                    expand=True,
                                    alignment=MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3
                                        ),
                                        Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3
                                        ),
                                        Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3
                                        ),
                                        Container(
                                            border_radius=20,
                                            padding=5,
                                            expand=True,
                                            bgcolor=self.color_teal,
                                            col=3
                                        )
                                    ]
                                )
                            ]
                        )
                    ),
                    Container(
                        bgcolor=self.color_teal,
                        padding=5,
                        border_radius=10,
                        height=80,
                        alignment=alignment.center,
                        content=ResponsiveRow(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                Container(
                                    expand=True,
                                    #height=80,
                                    col={"sm":5, "md":6},
                                    #bgcolor="blue",
                                    border_radius=5,
                                    #alignment=alignment.center,
                                    padding=5,
                                    content=Column([Text("Otras ciudades")], alignment=MainAxisAlignment.CENTER)
                                ),
                                #Text("Otras ciudades"),
                                Container(
                                    bgcolor=self.color_teal,
                                    #padding=5,
                                    col={"sm":7, "md":6, "lg":4},
                                    alignment=alignment.center,
                                    content=Dropdown(
                                        border_color="transparent",
                                        border_radius=20,
                                        #width=150,
                                        alignment=alignment.center,
                                        hint_text="Ciudades",
                                        hint_style=TextStyle(size=13),
                                        options=[
                                            dropdown.Option("Piura"),
                                            dropdown.Option("Lima"),
                                            dropdown.Option("Arequipa")
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    Container(
                        expand=True,
                        border_radius=10,
                        #padding=5,
                        alignment=alignment.center,
                        content=Column(
                            scroll="auto",
                            controls=[
                                ResponsiveRow(
                                    controls=[
                                        Container(bgcolor=self.color_teal,
                                                  border_radius=10,
                                                  padding=5,
                                                  height=100,
                                                  col={"md":12, "lg":6}),
                                        Container(bgcolor="red",
                                                  border_radius=10,
                                                  padding=5,
                                                  height=100,
                                                  col={"md":12, "lg":6}),
                                        Container(bgcolor="blue",
                                                  border_radius=10,
                                                  padding=5,
                                                  height=100,
                                                  col={"md":12, "lg":6}),
                                        Container(bgcolor=self.color_teal,
                                                  border_radius=10,
                                                  padding=5,
                                                  height=100,
                                                  col={"md":12, "lg":6})
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        )
    
        self.controls = [
            self.nav_container,
            self.frame_2,
            self.frame_3
        ]
    
    def switch_page(self, e):
        index = e.control.selected_index
        self.container_1.content = self.container_list_1[index]
        self.container_2.content = self.container_list_2[index]
        self.update()
    
    def mode_theme(self, e):
        if e.control.value:
            self.page.theme_mode = "dark"
        else:
            self.page.theme_mode = "light"
        self.page.update()


def main(page: Page):
    page.window.min_height = 650
    page.window.min_width = 600
    #page.window.maximizable = False
    page.theme = Theme(font_family="Monserrat")
    page.theme_mode = ThemeMode.SYSTEM
    ui = UI(page)
    page.add(ui)

app(main)
