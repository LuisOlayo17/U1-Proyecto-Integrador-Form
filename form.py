import flet as ft
import re

def main(page: ft.Page):
    # --- CONFIGURACIÓN ---
    page.title = "Registro de Estudiantes - Tap"
    page.bgcolor = "#F1F5F9"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    COLOR_PRIMARIO = "#2563EB"
    COLOR_SECUNDARIO = "#10B981"
    COLOR_BORDE = "#64748B"
    COLOR_ERROR = "#EF4444"

    def cerrar_dialogo(e):
        dlg_resumen.open = False
        page.update()

    dlg_resumen = ft.AlertDialog(
        title=ft.Text("Registro exitoso 🎉", color=COLOR_PRIMARIO),
        content=ft.Text(""),
        actions=[ft.TextButton("Cerrar", on_click=cerrar_dialogo)],
    )

    # 🔒 FUNCIÓN: elimina números mientras escribe (PERMITE BORRAR)
    def limpiar_nombre(e):
        nuevo_valor = re.sub(r"\d", "", e.control.value)
        if e.control.value != nuevo_valor:
            e.control.value = nuevo_valor
            page.update()

    # --- INPUTS ---
    txt_nombre = ft.TextField(
        label="Nombre",
        border_color=COLOR_BORDE,
        focused_border_color=COLOR_PRIMARIO,
        expand=True,
        on_change=limpiar_nombre  # 👈 AQUÍ LA SOLUCIÓN
    )

    txt_control = ft.TextField(
        label="Número de control",
        border_color=COLOR_BORDE,
        focused_border_color=COLOR_PRIMARIO,
        expand=True,
        input_filter=ft.NumbersOnlyInputFilter()
    )

    txt_email = ft.TextField(
        label="Email",
        border_color=COLOR_BORDE,
        focused_border_color=COLOR_PRIMARIO,
        expand=True
    )

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color=COLOR_BORDE,
        focused_border_color=COLOR_PRIMARIO,
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Ingeniería Mecatrónica"),
            ft.dropdown.Option("Ingeniería en Gestión Empresarial"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        expand=True,
        border_color=COLOR_BORDE,
        focused_border_color=COLOR_PRIMARIO,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 10)]
    )

    # --- GÉNERO ---
    rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino", fill_color=COLOR_SECUNDARIO),
            ft.Radio(value="Femenino", label="Femenino", fill_color=COLOR_SECUNDARIO),
            ft.Radio(value="Otro", label="Otro", fill_color=COLOR_SECUNDARIO),
            ft.Radio(value="Therian", label="Therian", fill_color=COLOR_SECUNDARIO),
        ])
    )

    txt_error_genero = ft.Text("", color=COLOR_ERROR, size=12)

    def es_email_valido(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def validar_y_enviar(e):
        campos = [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]
        hay_error = False

        for campo in campos:
            if not campo.value or campo.value.strip() == "":
                campo.error_text = "Este campo es obligatorio"
                campo.border_color = COLOR_ERROR
                hay_error = True
            else:
                campo.error_text = None
                campo.border_color = COLOR_BORDE

        if not hay_error and not es_email_valido(txt_email.value):
            txt_email.error_text = "Correo no válido"
            txt_email.border_color = COLOR_ERROR
            hay_error = True

        if not rg_genero.value:
            txt_error_genero.value = "Debes seleccionar un género"
            hay_error = True
        else:
            txt_error_genero.value = ""

        if not hay_error:
            resumen = (
                f"Nombre completo: {txt_nombre.value}\n"
                f"Número de control: {txt_control.value}\n"
                f"Correo electrónico: {txt_email.value}\n"
                f"Carrera elegida: {dd_carrera.value}\n"
                f"Semestre actual: {dd_semestre.value}\n"
                f"Género: {rg_genero.value}"
            )

            dlg_resumen.content = ft.Text(resumen)
            dlg_resumen.open = True
            if dlg_resumen not in page.overlay:
                page.overlay.append(dlg_resumen)

        page.update()

    # --- BOTÓN ---
    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="white", size=16, weight="bold"),
        bgcolor=COLOR_PRIMARIO,
        width=page.width,
        on_click=validar_y_enviar
    )

    # --- UI ---
    page.add(
        ft.Column([
            ft.Text("Formulario de Registro", size=26, weight="bold", color=COLOR_PRIMARIO),
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            ft.Column([
                ft.Text("Género:", color=COLOR_PRIMARIO, weight="bold"),
                rg_genero,
                txt_error_genero
            ], spacing=5),
            ft.Divider(height=20, color="transparent"),
            btn_enviar
        ], spacing=15)
    )

if __name__ == "__main__":
    ft.app(target=main)