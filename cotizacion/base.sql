"""---crear base de datos---"""
CREATE DATABASE IF NOT EXISTS cotizacion;
use cotizacion;

"""---crear tablas---"""
CREATE TABLE usuarios(
    id          int(25) auto_increment not null,
    idEmpledo   int(25) not null
    nombre      varchar(255),
    apellidos   varchar(255),
    email       varchar(255) not null,
    password    varchar(255) not null,
    fecha       date not null,
    CONSTRAINT  pk_usuarios PRIMARY KEY(id), """ asignar cual campo sera la llave primaria"""
    CONSTRAINT  uq_empleado UNIQUE(idEmpleado) """restriccion para no registrar usuarios con el mismo email"""
)ENGINE = InnoDB; """ mantener relacion entre tablas """

CREATE TABLE notas(
    id          int(25) auto_increment not null,
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    descripcion MEDIUMTEXT,
    fecha       date not null,
    CONSTRAINT  pk_notas PRIMARY KEY(id), """ asignar cual campo sera la llave primaria"""
    CONSTRAINT  fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id) """ asignar cual campo sera la llave foranea y hacer referencia a la llave primeria de usuario"""
)ENGINE = InnoDB