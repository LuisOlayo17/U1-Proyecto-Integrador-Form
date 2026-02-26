# U1 – PROYECTO INTEGRADOR  
## Formulario de Registro de Estudiantes con Validaciones (Flet + Python)

---

# Descripción del Proyecto

Este proyecto consiste en el desarrollo de un formulario de registro de estudiantes utilizando la librería **Flet en Python**.  

El objetivo fue mejorar un formulario básico agregando validaciones y controles solicitados en la actividad.

El sistema permite registrar:

- Nombre
- Número de control
- Email
- Carrera
- Semestre
- Género

Además, al presionar el botón **Enviar**, se muestra un resumen en una ventana modal (AlertDialog).

---

# Tecnologías utilizadas

- Python  
- Flet  
- Expresiones regulares (re)

---

# Explicación Paso a Paso

## 1. Importación de Librerías

Se importan:

- `flet`: para crear la interfaz gráfica.
- `re`: para validar el correo y limpiar el nombre.

---

## 2. Configuración de la Página

Se personaliza:

- Título de la ventana
- Color de fondo
- Espaciado
- Tema claro
- Colores personalizados para mantener un diseño uniforme

---

## 3. Campo Nombre (Validación automática)

Se creó la función `limpiar_nombre()` que:

- Elimina números mientras el usuario escribe.
- Permite borrar sin errores.
- Usa una expresión regular para filtrar dígitos.

✔ No permite números en el nombre.

---

## 4. Campo Número de Control

- Solo permite números.
- Usa `NumbersOnlyInputFilter()`.
- Es obligatorio.

✔ Evita que el usuario escriba letras.

---

## 5. Campo Email

Se valida usando una expresión regular:

- Debe contener "@"
- Debe tener dominio
- Debe incluir un punto

Si no cumple, muestra:

> "Correo no válido"

---

## 6. Control Dropdown

Se agregaron dos listas desplegables:

- Carrera (5 opciones)
- Semestre (1 al 9)

✔ Cumple con el requisito de incluir Dropdown.

---

## 7. Control Radio

Se agregó un grupo de botones tipo radio para el género.

Si no se selecciona uno, aparece mensaje de error.

✔ Cumple con el requisito de incluir Radio.

---

## 8. Validación de Campos Vacíos

Antes de enviar:

- Se verifica que ningún campo esté vacío.
- Si está vacío:
  - Se pone borde rojo.
  - Se muestra mensaje "Este campo es obligatorio".

✔ No permite entradas vacías.

---

## 9. Ventana Modal (AlertDialog)

Cuando todo es correcto:

- Se genera un resumen con los datos.
- Se muestra en una ventana modal.
- Incluye botón para cerrar.

✔ Cumple con el requisito solicitado.

---

## 10. Ejecución del Proyecto (Paso a Paso)

Para ejecutar correctamente el formulario es necesario **copiar el código completo** en un compilador o editor de Python.  
En este proyecto se utilizó **Visual Studio Code (VS Code)**.

Pasos para la ejecución:

1. Crear un archivo llamado `main.py`.
2. Copiar **todo el código completo** del proyecto dentro del archivo.
3. Guardar el archivo.
4. Abrir **Git Bash** en la carpeta donde se encuentra `main.py`.
5. Ejecutar los siguientes comandos:

```bash
cd ruta/del/proyecto
python main.py
```

Al ejecutarse, Flet mostrará una dirección local similar a:
http://127.0.0.1:60494
Al abrirla en el navegador se visualizará el formulario funcionando correctamente.

Durante la ejecución pueden aparecer mensajes de advertencia (DeprecationWarning).
Estos mensajes no afectan el funcionamiento del programa.

# 💻 Código Completo
```
import flet as ft
import re

def main(page: ft.Page):
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

    def limpiar_nombre(e):
        nuevo_valor = re.sub(r"\d", "", e.control.value)
        if e.control.value != nuevo_valor:
            e.control.value = nuevo_valor
            page.update()

    txt_nombre = ft.TextField(
        label="Nombre",
        border_color=COLOR_BORDE,
        focused_border_color=COLOR_PRIMARIO,
        expand=True,
        on_change=limpiar_nombre
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

    btn_enviar = ft.ElevatedButton(
        content=ft.Text("Enviar", color="white", size=16, weight="bold"),
        bgcolor=COLOR_PRIMARIO,
        width=page.width,
        on_click=validar_y_enviar
    )

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
```

# Conclusión
En este proyecto se logró desarrollar un formulario funcional con validaciones completas, evitando errores comunes como campos vacíos o correos mal escritos.

Se implementaron correctamente controles Dropdown y Radio, así como una ventana modal que muestra el resumen de los datos capturados.

Este proyecto demuestra el uso práctico de Flet para crear interfaces gráficas modernas en Python aplicando buenas prácticas de validación.

# Evidencias
<img width="1362" height="702" alt="image" src="https://github.com/user-attachments/assets/74a1f9cf-043b-4683-8151-9c7441780e4e" />
<img width="1359" height="707" alt="image" src="https://github.com/user-attachments/assets/5acb1064-5f06-4592-937b-a97831725491" />

