create database PROJECTO_FINAL;

create table plataforma(
codigo_de_plataforma varchar(25) primary key not null,
nombre varchar(25) not null,
tipo_de_conexion varchar (25) not null
);

create table articulo(
id_articulo int primary key not null,
nombre varchar(50) not null,
tipo varchar(25) not null,
estado varchar(25),
valoracion varchar(25) not null,
pais_de_envio varchar(25) not null,
peso varchar(50) not null,
tamaño varchar(50) not null,
marca varchar(25) not null,
nombre_de_usuario varchar(50) not null,
codigo_de_plataforma varchar(25),
foreign key (codigo_de_plataforma) references plataforma(codigo_de_plataforma)
);

create table empleados(
id_cliente int primary key not null,
nombre varchar(50) not null,
apellido varchar(50) not null,
edad int not null,
cargo varchar(50) not null,
);

create table tienda(
codigo_de_tienda varchar(25) primary key not null,
nombre varchar(25) not null,
telefono varchar(10) not null,
id_articulo int,
id_cliente int,
foreign key (id_articulo) references articulo(id_articulo),
foreign key (id_cliente) references empleados(id_cliente)
);

create table medio_de_transporte(
codigo_de_envio bigint primary key not null,
fecha_de_entrega date not null,
tipo_de_entrega varchar(25) not null,
tipo_de_paquete varchar(25),
codigo_de_tienda varchar(25),
foreign key (codigo_de_tienda) references tienda(codigo_de_tienda)
);

create table clientes(
id_cliente int primary key not null,
nombre varchar(50) not null,
apellido varchar(50) not null,
edad int not null,
fecha_de_nacimiento date not null,
direccion varchar(100) not null,
telefono varchar(10) not null,
mail varchar(50) not null,
nombre_usuario varchar(50) not null,
Contraseña varchar(50) not null,
codigo_de_envio bigint,
codigo_de_tienda varchar(25),
foreign key (codigo_de_tienda) references tienda(codigo_de_tienda),
foreign key (codigo_de_envio) references medio_de_transporte(codigo_de_envio)
);
CREATE UNIQUE NONCLUSTERED INDEX nombre_usuario
ON clientes(nombre_usuario);

CREATE UNIQUE NONCLUSTERED INDEX mail
ON clientes(mail);

CREATE UNIQUE NONCLUSTERED INDEX telefono
ON clientes(telefono);

insert into articulo(id_articulo,nombre,tipo,estado,valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario) values (12345,'nike 360','zapatillas','nuevo','muy buena','usa','2 lb','12 plg','nike','midrath')
insert into articulo(id_articulo,nombre,tipo,estado,valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario) values (54321,'adidas 360','zapatillas','nuevo','muy buena','usa','2 lb','12 plg','adidas','byluther')
insert into articulo(id_articulo,nombre,tipo,estado,valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario) values (67890,'nintendo switch','consola','nuevo','muy buena','china','5 lb','25 cm','nintendo','midrath')
