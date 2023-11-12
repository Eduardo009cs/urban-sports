

create table dimensionPosicion(
	id_posicion int IDENTITY(1,1) primary key,
	ofensiva int,
	descripcion varchar (20),
	descripcion_larga varchar (150)
);

create table dimensionJugador(
	id_jugador int IDENTITY(1,1) primary key,
	nombre varchar (150) not null,
	numero int,
	talla int, 
	peso float,
	fecha_naciemiento date,
	id_posicion_oficial int,

	constraint fk_posicion foreign key (id_posicion_oficial) references dimensionPosicion(id_posicion)

);


create table dimensionTipoEtapa(
	id_etapa int IDENTITY(1,1) primary key,
	nombre_etapa varchar(50),
	descripcion varchar (50)
);

create table dimensionTipoJugada(
	id_tipo_jugada int IDENTITY(1,1) primary key,
	nombre_tipo_jugada varchar(50)
);

create table dimensionTipoPartido(
	id_tipo_partido int IDENTITY(1,1) primary key,
	descripcion varchar(150)
);

create table dimensionEquipo(
	id_equipo int IDENTITY(1,1) primary key,
	nombre varchar(50),
	nombre_extendido varchar (50)
);

create table dimensionUbicacion(
	id_ubicacion int IDENTITY(1,1) primary key,
	valor varchar(50),
	latitud float,
	longitud float
);

create table dimensionTiempo(
	id_fecha int IDENTITY(1,1) primary key,
	fecha date,
	hora time(0),
	anio int,
	mes int,
	dia_semana int
);


create table dimensionTemporada(
	id_temporada int IDENTITY(1,1) primary key,
	descripcion varchar(50),
	id_fecha_inicio int,
	id_fecha_final int
	constraint fk_fecha_inicio foreign key (id_fecha_inicio) references dimensionTiempo(id_fecha),
	constraint fk_fecha_final foreign key (id_fecha_final) references dimensionTiempo(id_fecha)
);																								


create table dimensionTipoMedicion(
	id_medicion int IDENTITY(1,1) primary key,
	descripcion varchar(50),
	descripcion_larga varchar (150)
);

create table dimensionTipoMedicionBiometrica(
	id_medicion_biometrica int IDENTITY(1,1) primary key,
	descripcion varchar (50),
	unidad varchar(20)
);

create table dimensionTipoSensor(
	id_sensor int IDENTITY(1,1) primary key,
	marca varchar(50),
	nombre varchar (50),
	modelo varchar(50)
);


create table tabHechos_Partido(
	id_partido int IDENTITY(1,1) primary key,
	id_tipo_partido int,
	puntos_favor int,
	puntos_contra int,
	id_equipo_local int,
	id_equipo_visita int,
	id_ubicacion int,
	id_temporada int,
	id_fecha int,
	constraint fk_tipo_partido foreign key (id_tipo_partido) references dimensionTipoPartido(id_tipo_partido),
	constraint fk_equipo_local foreign key (id_equipo_local) references dimensionEquipo(id_equipo),
	constraint fk_equipo_visita foreign key (id_equipo_visita) references dimensionEquipo(id_equipo),
	constraint fk_ubicacion foreign key (id_ubicacion) references dimensionUbicacion(id_ubicacion),
	constraint fk_temporada foreign key (id_temporada) references dimensionTemporada(id_temporada),
	constraint fk_fecha foreign key (id_fecha) references dimensionTiempo(id_fecha)

);


create table dimensionJugada(
	id_jugada int IDENTITY(1,1) primary key,
	id_tipo_etapa int,
	id_partido int,
	numero_jugada int,
	pre_snap int,
	desarrollo int,
	finish int,
	pride int,
	id_jugador int,
	id_tipo_jugada int,
	id_posicion int,
	constraint fk_tipo_etapa foreign key (id_tipo_etapa) references dimensionTipoEtapa(id_etapa),
	constraint fk_partido foreign key (id_partido) references tabHechos_Partido(id_partido),
	constraint fk_jugador foreign key (id_jugador) references dimensionJugador(id_jugador),
	constraint fk_tipo_jugada foreign key (id_tipo_jugada) references dimensionTipoJugada(id_tipo_jugada),
	constraint fk_posicion1 foreign key (id_posicion) references dimensionPosicion(id_posicion)
);


create table tabHechos_EstadisticasProductividad(
	id_evaluacion int IDENTITY(1,1) primary key,
	id_jugador int,
	id_tipo_medicion int,
	valor int,
	id_partido int,
	id_posicion int,
	
	constraint fk_jugador_p foreign key (id_jugador) references dimensionJugador(id_jugador),
	constraint fk_tipo_medicion foreign key (id_tipo_medicion) references dimensionTipoMedicion(id_medicion),
	constraint fk_partido_p foreign key (id_partido) references tabHechos_Partido(id_partido),
	constraint fk_posicion_p foreign key (id_posicion) references dimensionPosicion(id_posicion)
);

create table tabHechos_Biometria(
	id_biometria int IDENTITY(1,1) primary key,
	id_tipo_medicion_biometrica int,
	valor int,
	id_partido int,
	id_tipo_sensor int,
	id_jugador int,
	
	constraint fk_tipo_medicion_biometrica foreign key (id_tipo_medicion_biometrica) references dimensionTipoMedicionBiometrica(id_medicion_biometrica),
	constraint fk_partido_b foreign key (id_partido) references tabHechos_Partido(id_partido),
	constraint fk_sensor foreign key (id_tipo_sensor) references dimensionTipoSensor(id_sensor),
	constraint fk_jugador_b foreign key (id_jugador) references dimensionJugador(id_jugador)
);


