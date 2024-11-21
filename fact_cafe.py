from tkinter import *
import os
import random
import datetime
from tkinter import filedialog, messagebox

#Precios sin IVA
operador = ''
precios_cafeteria = [2370, 2370, 2528, 2212, 3081, 3081, 2212, 2370]
precios_panaderia = [2212, 2370, 2212, 1817, 1185, 2370, 3950, 3792]
precios_menues = [6162, 4740, 7347, 5135, 6636]


## FUNCIONES.

# Verificar si algun checkbutton esta activado "1", si es asi, habilita para colocar cantidad.
def revisar_check():
    x = 0
    for c in cuadros_cafe:
        # Si el checkbutton esta activado:
        if variables_cafe[x].get() == 1:
            # permitir colocar cantidad.
            cuadros_cafe[x].config(state=NORMAL)
            if cuadros_cafe[x].get() == '0':
                # borrar contenido.
                cuadros_cafe[x].delete(0, END)
            cuadros_cafe[x].focus()
        else:
            # Si no esta activado:
            cuadros_cafe[x].config(state=DISABLED)
            texto_cafe[x].set('0')
        x += 1

    x = 0
    for c in cuadros_panaderia:
        if variables_panaderia[x].get() == 1:
            cuadros_panaderia[x].config(state=NORMAL)
            if cuadros_panaderia[x].get() == '0':
                cuadros_panaderia[x].delete(0, END)
            cuadros_panaderia[x].focus()
        else:
            cuadros_panaderia[x].config(state=DISABLED)
            texto_panaderia[x].set('0')
        x += 1

    x = 0
    for c in cuadros_menues:
        if variables_menues[x].get() == 1:
            cuadros_menues[x].config(state=NORMAL)
            if cuadros_menues[x].get() == '0':
                cuadros_menues[x].delete(0, END)
            cuadros_menues[x].focus()
        else:
            cuadros_menues[x].config(state=DISABLED)
            texto_menues[x].set('0')
        x += 1


def total():
    sub_total_cafeteria = 0
    p = 0
    for cantidad in texto_cafe:
        sub_total_cafeteria = sub_total_cafeteria + (float(cantidad.get()) * precios_cafeteria[p])
        p += 1

    sub_total_panaderia = 0
    p = 0
    for cantidad in texto_panaderia:
        sub_total_panaderia = sub_total_panaderia + (float(cantidad.get()) * precios_panaderia[p])
        p += 1

    sub_total_menues = 0
    p = 0
    for cantidad in texto_menues:
        sub_total_menues = sub_total_menues + (float(cantidad.get()) * precios_menues[p])
        p += 1


#Calculo IVA volver al precio del producto y generamos el IVA

    sub_total = sub_total_cafeteria + sub_total_panaderia + sub_total_menues
    impuestos = ((sub_total * 21)/79)
    total = sub_total + impuestos

    var_costo_cafes.set(f'$ {round(sub_total_cafeteria, 2)}')
    var_costo_panaderia.set(f'$ {round(sub_total_panaderia, 2)}')
    var_costo_menues.set(f'$ {round(sub_total_menues, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

# Generar recibo.
def recibo():
    # variables globales para generar el cliente.
    global nombre_cliente, telefono_cliente;
    
    texto_recibo.delete(1.0, END)
    # Nombre cafeteria.
    texto_recibo.insert(END,'\t"CAFE DE ESPECIALITACC"\n')
    
    # datos cliente.
    nombre = nombre_cliente.get()
    telefono = telefono_cliente.get()
    
    if nombre and telefono:
        texto_recibo.insert(END, f"Cliente: {nombre}\n")
        texto_recibo.insert(END, f"Telefono: {telefono}\n")
    elif telefono:
        texto_recibo.insert(END, f"Telefono: {telefono}\n")
    elif nombre:
        texto_recibo.insert(END, f"Cliente: {nombre}\n")
    else:
        texto_recibo.insert(END, "Cliente: No especificado.\n")

    # numero de recibo.
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    
    # fecha del momento.
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'\nDatos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for cafeteria in texto_cafe:
        if cafeteria.get() != '0':
            texto_recibo.insert(END, f'{lista_cafes[x]}\t\t{cafeteria.get()}\t'
                                     f'$ {int(cafeteria.get()) * precios_cafeteria[x]}\n')
        x += 1

    x = 0
    for panaderia in texto_panaderia:
        if panaderia.get() != '0':
            texto_recibo.insert(END, f'{lista_panaderia[x]}\t\t{panaderia.get()}\t'
                                     f'$ {int(panaderia.get()) * precios_panaderia[x]}\n')
        x += 1

    x = 0
    for menu in texto_menues:
        if menu.get() != '0':
            texto_recibo.insert(END, f'{lista_menues[x]}\t\t{menu.get()}\t'
                                     f'$ {int(menu.get()) * precios_menues[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo Cafeterìa: \t\t\t{var_costo_cafes.get()}\n')
    texto_recibo.insert(END, f' Costo Panadería: \t\t\t{var_costo_panaderia.get()}\n')
    texto_recibo.insert(END, f' Costo Menús: \t\t\t{var_costo_menues.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' IVA: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')
    
    #Limpiar entradas de cliente.
    nombre_cliente.set("")
    telefono_cliente.set("")

# Guardar recibo.
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')

# Resetear todos los parametros.
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_cafe:
        texto.set('0')
    for texto in texto_panaderia:
        texto.set('0')
    for texto in texto_menues:
        texto.set('0')

    for cuadro in cuadros_cafe:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_panaderia:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_menues:
        cuadro.config(state=DISABLED)

    for v in variables_cafe:
        v.set(0)
    for v in variables_panaderia:
        v.set(0)
    for v in variables_menues:
        v.set(0)

    var_costo_cafes.set('')
    var_costo_panaderia.set('')
    var_costo_menues.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

# Ruta base para poder poner imagenes.
ruta_base = os.path.dirname(os.path.abspath(__file__))


# tamaño de la ventana
aplicacion.geometry('1248x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# imagen cafe.
#ruta de la imagen.
ruta_imagen_cafe = os.path.join(ruta_base, "img", "mini_cafe.png")

# Verificar si la imagen existe en la ruta
if os.path.exists(ruta_imagen_cafe):
    print("La imagen está en la ruta correcta:", ruta_imagen_cafe)
    img = PhotoImage(file=ruta_imagen_cafe)
else:
    print("No se encuentra la imagen en la ruta especificada:", ruta_imagen_cafe)

# icono ventana
aplicacion.iconphoto(True, img)

# titulo de la ventana
aplicacion.title('Facturación "Café EspecialiTACC" ')

# color de fondo de la ventana
aplicacion.config(bg='bisque')

# panel superior
panel_superior = Frame(
    aplicacion,
    bd=1,
    relief=RAISED)

panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(
    panel_superior,
    text='FACTURACIÓN - Café EspecialiTACC',
    fg='DarkOrange4',
    font=('Bahnschrift', 40, 'bold'),
    bg='burlywood1',
    width=40)

etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(
    aplicacion,
    bd=1,
    relief=FLAT,
    bg="burlywood")

panel_izquierdo.pack(side=LEFT,  padx=15)

# panel costos
panel_costos = Frame(
    panel_izquierdo,
    bd=1,
    relief=FLAT,
    bg='burlywood1',
    pady=7,
    padx=30)

panel_costos.pack(side=BOTTOM, fill='both')


# panel MENUES
panel_menues = LabelFrame(
    panel_izquierdo,
    text='MENÚS',
    font=('Dosis', 19, 'bold'),
    bd=1,
    relief=FLAT,
    fg='DarkOrange4',
    pady=5,
    bg='tan3',
    labelanchor='n')

panel_menues.pack(side=LEFT, fill='both', padx=1)

# panel PANADERIAS
panel_panaderias = LabelFrame(
    panel_izquierdo,
    text='PANADERÍA',
    font=('Dosis', 19, 'bold'),
    bd=1,
    relief=FLAT,
    fg='DarkOrange4',
    pady=5,
    bg='tan2',
    labelanchor='n')

panel_panaderias.pack(side=LEFT, fill='both', padx=1)

# panel CAFES
panel_cafes = LabelFrame(
    panel_izquierdo,
    text='CAFETERÍA',
    font=('Dosis', 19, 'bold'),
    bd=1,
    relief=FLAT,
    fg='DarkOrange4',
    pady=5,
    bg='tan3',
    labelanchor='n')

panel_cafes.pack(side=LEFT, fill='both', padx=1)

# panel derecha
panel_derecha = Frame(
    aplicacion,
    bd=1,
    relief=FLAT,
    bg='bisque')

panel_derecha.pack(side=RIGHT)

# Aplicar imagen
label_img = Label(panel_derecha, image= img, bg='bisque')
label_img.pack()

# panel recibo
panel_recibo = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg='burlywood')

panel_recibo.pack()

# panel botones
panel_botones = Frame(
    panel_derecha,
    bd=1,
    relief=FLAT,
    bg='burlywood')

panel_botones.pack()

# Variables globales para datos del cliente
nombre_cliente = StringVar()
telefono_cliente = StringVar()

# Etiquetas y entradas para el nombre y telefono del cliente.
# nombre
panel_nombre = Label(
    panel_derecha,
    text="Nombre del cliente: ",
    pady=10,
    bg='bisque',
    font=('Dosis', 11, 'bold')
)

panel_nombre.pack(side=LEFT)

# input nombre
Entry(panel_derecha, textvariable=nombre_cliente).pack(side=LEFT, pady=10)

#telefono
panel_telefono = Label(
    panel_derecha,
    text="Telefono del cliente: ",
    pady=10,
    bg='bisque',
    font=('Dosis', 11, 'bold')
    )
panel_telefono.pack(side=LEFT)

#input telefono
Entry(panel_derecha, textvariable=telefono_cliente).pack(side=LEFT, pady=10, padx= 5)


# lista de cafeteria
lista_cafes = ['Expresso',
               'Americano',
               'Macchiato',
               'Flat White',
               'Capuccino',
               'Latte',
               'Té en hebras',
               'Jugos naturales'] 

# Lista de panaderia
lista_panaderia = [
    'Croissant',
    'New York Roll',
    'Cinnamon Roll',
    'Masas Finas x3',
    'Cookies',
    'Chipa',
    'Avocado Toast',
    'French Toast']

# Lista de menus
lista_menues = ['Menú Ligero',
                'Menú Classic',
                'Menú Toast',
                'Menú Roll',
                'Menú TACC']

# Descripcion menus
descripcion_menus = ['Infusión + 2 Cookies',
                     'Infusión + 2 Medialunas',
                     'Infusión + Toast a elección',
                     'Infusión + Roll a elección',
                     'Infusión + Torta a elección',]

# generar items cafeteria
variables_cafe = []
cuadros_cafe = []
texto_cafe = []
contador = 0
for cafe in lista_cafes:
    # crear checkbutton
    variables_cafe.append('')
    variables_cafe[contador] = IntVar()
    cafe = Checkbutton(panel_cafes,
                         text=cafe.title(),
                         font=('Dosis', 12, 'bold',),
                         bg='tan3',
                         onvalue=1,
                         offvalue=0,
                         variable=variables_cafe[contador],
                         command=revisar_check)

    cafe.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_cafe.append('')
    texto_cafe.append('')
    texto_cafe[contador] = StringVar()
    texto_cafe[contador].set('0')
    cuadros_cafe[contador] = Entry(panel_cafes,
                                     font=('Dosis', 12, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_cafe[contador])
    cuadros_cafe[contador].grid(row=contador,
                                  column=1)
    contador += 1

# generar items panaderia
variables_panaderia = []
cuadros_panaderia = []
texto_panaderia = []
contador = 0
for panaderia in lista_panaderia:
    # crear checkbutton
    variables_panaderia.append('')
    variables_panaderia[contador] = IntVar()
    panaderia = Checkbutton(panel_panaderias,
                         text=panaderia.title(),
                         font=('Dosis', 12, 'bold',),
                         bg='tan2',
                         onvalue=1,
                         offvalue=0,
                         variable=variables_panaderia[contador],
                         command=revisar_check)
    panaderia.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_panaderia.append('')
    texto_panaderia.append('')
    texto_panaderia[contador] = StringVar()
    texto_panaderia[contador].set('0')
    cuadros_panaderia[contador] = Entry(panel_panaderias,
                                     font=('Dosis', 12, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_panaderia[contador])
    cuadros_panaderia[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items menus
variables_menues = []
cuadros_menues = []
texto_menues = []
contador = 0
## ID y valor de cada menu.
for id, menues in enumerate(lista_menues):
    # crear checkbutton
    variables_menues.append('')
    variables_menues[contador] = IntVar()
    menues = Checkbutton(panel_menues,
                          text=menues.title(),
                          font=('Dosis', 12, 'bold'),
                          bg='tan3',
                          onvalue=1,
                          offvalue=0,
                          variable=variables_menues[contador],
                         command=revisar_check)

    ## Colocar los menu en filas par (0,2,4,6,8) de la columna 0. 
    menues.grid(row=contador * 2,
                 column=0,
                 sticky=W)
    
    descripcion_label = Label(panel_menues,
                              text=descripcion_menus[id],
                              font=('Dosis', 11, 'bold'),
                              bg='tan3',
                              fg='white')
    ## Colocar descripcion en filas impar (1,3,5,7,9) de la columna 0.
    descripcion_label.grid(row=contador * 2 + 1, column=0, sticky=W)
                        
    
    
    # crear los cuadros de entrada
    cuadros_menues.append('')
    texto_menues.append('')
    texto_menues[contador] = StringVar()
    texto_menues[contador].set('0')
    cuadros_menues[contador] = Entry(panel_menues,
                                      font=('Dosis', 12, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_menues[contador])
    cuadros_menues[contador].grid(row=contador * 2,
                                   column=1)
    contador += 1


# variables
var_costo_cafes = StringVar()
var_costo_panaderia = StringVar()
var_costo_menues = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
 ## etiqueta costo cafes.
etiqueta_costo_cafes = Label(panel_costos,
                              text='Costo Cafeteria',
                              font=('Dosis', 12, 'bold'),
                              bg='burlywood1',
                              fg='DarkOrange4')
etiqueta_costo_cafes.grid(row=0, column=0)
 ## texto costo cafes.
texto_costo_cafes = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_cafes)
texto_costo_cafes.grid(row=0, column=1, padx=41)

## etiqueta costo panaderia.
etiqueta_costo_panaderia = Label(panel_costos,
                              text='Costo Panaderia',
                              font=('Dosis', 12, 'bold'),
                              bg='burlywood1',
                              fg='DarkOrange4')
etiqueta_costo_panaderia.grid(row=1, column=0)
 ## texto costo panaderia.
texto_costo_panaderia = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_panaderia)
texto_costo_panaderia.grid(row=1, column=1, padx=41)

 ## etiqueta costo menus.
etiqueta_costo_menues = Label(panel_costos,
                              text='Costo Menu',
                              font=('Dosis', 12, 'bold'),
                              bg='burlywood1',
                              fg='DarkOrange4')
etiqueta_costo_menues.grid(row=2, column=0)
 ## texto costo menus.
texto_costo_menues = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_menues)
texto_costo_menues.grid(row=2, column=1, padx=41)

 ## etiqueta subtotal.
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='burlywood1',
                              fg='DarkOrange4')
etiqueta_subtotal.grid(row=0, column=2)
 ## texto subtotal.
texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

 ## etiqueta IVA.
etiqueta_impuestos = Label(panel_costos,
                              text='IVA',
                              font=('Dosis', 12, 'bold'),
                              bg='burlywood1',
                              fg='DarkOrange4')
etiqueta_impuestos.grid(row=1, column=2)
 ## texto IVA.
texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

 ## etiqueta total.
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='burlywood1',
                              fg='DarkOrange4')
etiqueta_total.grid(row=2, column=2)
 ## texto total.
texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)


# Botones.
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='DarkOrange4',
                   bg='burlywood1',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)


# evitar que la pantalla se cierre
aplicacion.mainloop()