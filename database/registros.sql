insert into dimensionPosicion (ofensiva,descripcion,descripcion_larga)
values(1,'QB','Quarterback'),
	  (1,'WR','Wide Receiver ');


insert into dimensionJugador
values ('Emiliano Martinez',84,184,96,'1998-01-01',2),
	   ('Alfonso Plascencia',85,171,78.5,'1999-01-01',2),
	   ('Emilio Garcia',3,176,83,'1998-01-01',2),
	   ('Eduardo Moreno',83,180,80,'2001-01-01',2),
	   ('Emilio Mendez',17,175,89,'2000-01-01',2),
	   ('Erick Barrero',11,177,85,'2001-01-01',2),
	   ('Emiliano Flores',10,190,76,'2002-01-01',2),
	   ('Erick Estrada',14,182,82,'1999-01-01',2),
	   ('Emilio Alvarado',81,182,82,'1999-01-01',2),
	   ('Diego Alvarez',89,191,72,'1999-01-01',2),
	   ('Ricardo Sanchez',82,184,82,'1999-01-01',2),
	   ('Rodrigo Suarez',19,180,87,'2000-01-01',2),
	   ('Axel Medina',0,0,0,'2000-01-01',1),
	   ('Aldo Herrera',0,0,0,'2000-01-01',1),
	   ('Javier Lopez',0,0,0,'2000-01-01',1)
	   


insert into dimensionTipoPartido
values ('Partido')

insert into dimensionEquipo
values ('BB' , 'Burros Blancos')


insert into dimensionUbicacion
values ('Estadio Wilfrido',138.2,156.2)


insert into dimensionTiempo
values ('2022-07-17','00:00:00',2023,07,17),
		('2023-07-17','00:00:00',2023,07,17),
		('2023-05-17','12:45:25',2023,05,17);

insert into dimensionTemporada
values ('2023-2024',1,2)

insert into dimensionTipoEtapa
values ('Juego','Juego Oficial')
