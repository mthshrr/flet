import flet as ft


def main(page: ft.Page):
   page.title = "Card de Produto"
   page.bgcolor = "#12151a"
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
   page.padding = 20


   def favoritar(e):
       favorito = e.control.icon == ft.Icons.FAVORITE_BORDER
       e.control.icon = ft.Icons.FAVORITE if favorito else ft.Icons.FAVORITE_BORDER
       e.control.icon_color = "#e2543a" if favorito else "white"
       e.control.update()


   def comprar(e):
       snack_bar = ft.SnackBar(
           content=ft.Text("Produto adicionado ao carrinho 🛒", color="#0d1210"),
           bgcolor="#7ee0c0",
       )
       page.open(snack_bar)


   card = ft.Container(
       width=320,
       bgcolor="#1b1f26",
       border_radius=18,
       padding=14,
       shadow=ft.BoxShadow(blur_radius=25, color="#59000000"),
       content=ft.Column(
           spacing=10,
           controls=[
               ft.Stack(
                   controls=[
                       ft.Container(
                           border_radius=14,
                           clip_behavior=ft.ClipBehavior.HARD_EDGE,
                           content=ft.Image(
                               src="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80",
                               width=292,
                               height=200,
                               fit="cover",
                           ),
                       ),
                       ft.Container(
                           content=ft.Text("25% OFF", size=11, weight=ft.FontWeight.BOLD, color="white"),
                           bgcolor="#e2543a",
                           padding=ft.Padding(8, 4, 8, 4),
                           border_radius=8,
                           margin=10,
                       ),
                       ft.Container(
                           alignment=ft.Alignment(1.0, -1.0),
                           margin=6,
                           content=ft.IconButton(
                               icon=ft.Icons.FAVORITE_BORDER,
                               icon_color="white",
                               on_click=favoritar,
                           ),
                       ),
                   ]
               ),
               ft.Row(
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   controls=[
                       ft.Text("Tênis Esportivo", size=12, color="#7b8794"),
                       ft.Row(
                           spacing=4,
                           controls=[
                               ft.Icon(ft.Icons.STAR, color="#f2b134", size=14),
                               ft.Text("4.8 (120)", size=12, color="#7b8794"),
                           ],
                       ),
                   ],
               ),
               ft.Text("Nike Air Zoom Pegasus Turbo", size=17, weight=ft.FontWeight.BOLD, color="white"),
               ft.Row(
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   controls=[
                       ft.Column(
                           spacing=0,
                           controls=[
                               ft.Text("R$ 599,99", size=12, color="#7b8794", style=ft.TextStyle(decoration=ft.TextDecoration.LINE_THROUGH)),
                               ft.Text("R$ 449,99", size=19, weight=ft.FontWeight.BOLD, color="#7ee0c0"),
                           ],
                       ),
                       ft.ElevatedButton(
                           content=ft.Text("Comprar"),
                           icon=ft.Icons.SHOPPING_CART_OUTLINED,
                           color="#0d1210",
                           bgcolor="#7ee0c0",
                           on_click=comprar,
                       ),
                   ],
               ),
           ],
       ),
   )


   page.add(card)


ft.app(target=main)

