create proc mostrar_articulos_del_cliente
@user varchar(50)
as
select id_articulo,nombre,tipo,estado,pais_de_envio,peso,tamaño,marca from articulo
where nombre_de_usuario=@user

exec mostrar_articulos_del_cliente @user='midrath'


-----------------------------------------

create view todos_los_articulos
as
select id_articulo, nombre,tipo,estado, valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario as 'propietario' from articulo

select * from todos_los_articulos

-----------------------------------------

create proc articulos_por_cliente
@user varchar(50)
as
select id_articulo, nombre,tipo,estado, valoracion,pais_de_envio,peso,tamaño,marca,nombre_de_usuario as 'propietario' from articulo
where nombre_de_usuario=@user

exec articulos_por_cliente @user='byluther'

------------------------------------------------

create proc eliminar_paquete
@id int
as
delete from articulo where id_articulo=@id

exec eliminar_paquete @id=785

------------------------------------------------


create proc ingresar_estado
@estado_nuevo varchar(25),
@estado_viejo varchar(25),
@id int
as
update articulo set estado=@estado_nuevo
where estado=@estado_viejo and id_articulo=@id

exec ingresar_estado @estado_nuevo='en transito', @estado_viejo= null, @id=789

------------------------------------------------


