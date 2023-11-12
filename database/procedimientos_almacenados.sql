create procedure insertIntoDimensionJugada

-- Procedemiento para insertar una jugada

-- Entrada del procedimiento
@inPresnap int,
@inDesarrollo int,
@inFinish int,
@inPride int, 
@inNumJugada int,
@inNombre varchar(20),
@inApellido varchar(20),
@inTipoEtapa varchar(20),
@inFecha date,
@tipoJugada varchar(100)

as

-- Variables

declare @idJugador int;
declare @idPosicion int;
declare @idEtapa int;
declare @idFecha int;
declare @idPartido int;
declare @idTipoJugada int;

-- Obtenemos el id de la fecha

select @idFecha = id_fecha
from dimensionTiempo
where fecha = @inFecha

-- Obtenemos el id del partido

select @idPartido = id_partido 
from tabHechos_Partido
where id_fecha = @idFecha

-- Obtenemos el id del tipo juagada

select @idTipoJugada = id_tipo_jugada
from dimensionTipoJugada 
where nombre_tipo_jugada = @tipoJugada

-- Si no existe una jugada se inserta en la tabla

if @idTipoJugada is null
begin 
insert into dimensionTipoJugada values(@tipoJugada)
end

-- Obtenemos de nuevo el id del tipo jugada

select @idTipoJugada = id_tipo_jugada
from dimensionTipoJugada 
where nombre_tipo_jugada = @tipoJugada

-- Obtenemos el id del jugador

select @idJugador = id_jugador, @idPosicion = id_posicion_oficial
from dimensionJugador
where Charindex(@inNombre, nombre) > 0 and CHARINDEX(@inApellido, nombre) > 0;

-- Obtenemos el id de la etapa

select @idEtapa = id_etapa 
from dimensionTipoEtapa
where nombre_etapa = @inTipoEtapa

-- Si no existe el registro lo ingresamos y seleccionamos

if @idEtapa is null 

begin

insert into dimensionTipoEtapa (@inTipoEtapa,@inTipoEtapa)

-- Obtenemos el id de la etapa

select @idEtapa = id_etapa 
from dimensionTipoEtapa
where nombre_etapa = @inTipoEtapa

end

-- Insertamos la jugada con los valores obtenenidos

insert into dimensionJugada
values (@idEtapa,@idPartido,@inNumJugada,@inPresnap,@inDesarrollo,@inFinish,@inPride,@idJugador,@idTipoJugada,@idPosicion)


go

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
create procedure insertIntoHechosPartido

-- Procedimiento para insertar en la tabla hechos partidos

-- Parametros de entrada

@inFecha date,
@inHora time,
@inTipoPartido varchar(50),
@inEquipoLocal varchar (10),
@inEquipoVisita varchar(10),
@inUbicacion varchar (50),
@inPuntosFavor int,
@inPuntosContra int 


as

-- Variables

declare @idTipoPartido int;
declare @idEquipoLocal int;
declare @idEquipoVisita int;
declare @idUbicacion int;
declare @idFecha int;
declare @idTemporada int;
declare @idPartido int;

-- Obtenemos el id de la Fecha 

select @idFecha= id_fecha 
from dimensionTiempo
where fecha = @inFecha 
and hora = @inHora

-- Obtenemos el id del partido

select @idPartido =  id_partido 
from tabHechos_Partido
where id_fecha = @idFecha

-- Verificamos si el registro del partido existe si no existe realizamos el registro

if @idPartido is null

begin

-- Obtenemos el id del tipo partido
select @idTipoPartido = id_tipo_partido 
from dimensionTipoPartido
where descripcion = @inTipoPartido

-- Obtenemos el id del equipo local

select @idEquipoLocal = id_equipo 
from dimensionEquipo
where nombre= @inEquipoLocal or nombre_extendido = @inEquipoLocal

-- Si no existe el regitro lo agregamos

if @idEquipoLocal is null

begin

insert into dimensionEquipo (nombre_extendido) values (@inEquipoLocal)

end

-- Obtenemos el id del equipo de Local

select @idEquipoVisita = id_equipo 
from dimensionEquipo
where nombre= @inEquipoVisita or nombre_extendido = @inEquipoVisita

-- Obtenemos el id del equipo visitante

select @idEquipoVisita = id_equipo 
from dimensionEquipo
where nombre= @inEquipoVisita or nombre_extendido = @inEquipoVisita

-- Si no existe el regitro lo agregamos

if @idEquipoVisita is null

begin

insert into dimensionEquipo (nombre_extendido) values (@inEquipoVisita)

end

-- Obtenemos el id del equipo de visita

select @idEquipoVisita = id_equipo 
from dimensionEquipo
where nombre= @inEquipoVisita or nombre_extendido = @inEquipoVisita


-- Obtenemos el id de la ubicación

select @idUbicacion = id_ubicacion
from dimensionUbicacion
where valor = @inUbicacion

-- Obtenemos el id de la temporada

select @idTemporada = id_temporada 
from dimensionTemporada
where descripcion = '2023-2024'

-- Insertamos el registro 

insert into tabHechos_Partido
values ( @idTipoPartido, @inPuntosFavor,@inPuntosContra, @idEquipoLocal,@idEquipoVisita,@idUbicacion,@idTemporada,@idFecha)

end

go

---------------------------------------------------------------------------------------------------------------------

create procedure insertIntoDimensionTiempo

-- Procedimiento de para agregar en la dimension tiempo

-- Parametros de entrada

@inFecha date,
@inHora time,
@inAnio int,
@inMes int,
@inDia int

as

-- Variables

declare @idTiempo int;

-- Obtenemos el id de la fecha

set @idTiempo = (select id_fecha 
from dimensionTiempo 
where fecha = @inFecha and 
mes = @inMes and
anio = @inAnio and
dia_semana = @inDia)

-- Verificamos si ya existe el registro

if @idTiempo is not null

-- Realizamos el un update en el registro de la fecha 

begin
update dimensionTiempo
set hora = @inHora
where fecha = @inFecha and 
mes = @inMes and
anio = @inAnio and
dia_semana = @inDia
end

else

-- Si no existe agregamos el registro

begin
insert into dimensionTiempo 
values (@inFecha,@inHora,@inAnio,@inMes,@inDia)
end

go

-----------------------------------------------------------------------------------------------------------------------------

create procedure insertIntoEstadisticasProductividad

-- Procedimiento para insertar estadisticas de productividad

-- Parametros de entrada

@inNombre varchar(20),
@inApellido varchar(20),
@inTipoEvaluacion varchar(20),
@inValorEvaluacion int,
@inFecha date

as

-- Variables

declare @idTipoMedicion int;
declare @idJugador int;
declare @idPosicion int;
declare @idPartido int;
declare @idFecha int;

-- Obtenemos el id de la fecha

select @idFecha = id_fecha 
from dimensionTiempo 
where fecha = @inFecha

-- Obtenemos el id del partido

select @idPartido =  id_partido
from tabHechos_Partido
where id_fecha = @idFecha

-- Obtenemos el id de la medicion

select @idTipoMedicion = id_medicion
from dimensionTipoMedicion
where descripcion_larga = @inTipoEvaluacion

-- Si no existe el registro lo agregamos

if @idTipoMedicion is null

begin
insert into dimensionTipoMedicion values (@inTipoEvaluacion,@inTipoEvaluacion)

-- Obtenemos el id del registro que acabamos de agregar

select @idTipoMedicion = id_medicion
from dimensionTipoMedicion
where descripcion_larga = @inTipoEvaluacion

end

-- Obtenemos el id del jugador

select @idJugador = id_jugador, @idPosicion = id_posicion_oficial
from dimensionJugador
where Charindex(@inNombre, nombre) > 0 and CHARINDEX(@inApellido, nombre) > 0;

-- Agregamos el registro en la estadisticas de productividad

insert into tabHechos_EstadisticasProductividad
values(@idJugador,@idTipoMedicion,@inValorEvaluacion,@idPartido,@idPosicion)

go


-----------------------------------------------------------------------------

select * from tabHechos_Biometria
select * from dimensionTipoSensor

create procedure insertIntoTabHechosBiometria

-- Procedimiento para insertar registros dentro de la tabla de hechos biometria

-- Parametros de entrada

@inFecha date,
@inNombre varchar(50),
@inApellido varchar (50),
@inModelo varchar (50),
@inTipoMedicion varchar (50),
@inValorMedicion int,
@inUnidad varchar(20)
as

-- Variables

declare @idTipoMedicion int
declare @idTipoSensor int
declare @idJugador int
declare @idPartido int
declare @idFecha int

-- Obtenemos el id de la fecha

select @idFecha = id_fecha 
from dimensionTiempo 
where fecha = @inFecha

-- Obtenemos el id del partido

select @idPartido =  id_partido
from tabHechos_Partido
where id_fecha = @idFecha

-- Obtenemos el id tipo del sensor 

select @idTipoSensor = id_sensor
from dimensionTipoSensor
where modelo = @inModelo

-- Verificamos si existe el registro, si no agregamos el registro

If @idTipoSensor is null

begin

-- Agregamos el registro del sensor

select * from dimensionTipoSensor
insert into dimensionTipoSensor values ('Garmin','VivoSmart 5',@inModelo)

-- Obtenemos el id tipo del sensor 

select @idTipoSensor = id_sensor
from dimensionTipoSensor
where modelo = @inModelo

end

-- Obtenemos el id del jugador

select @idJugador = id_jugador
from dimensionJugador
where Charindex(@inNombre, nombre) > 0 and CHARINDEX(@inApellido, nombre) > 0;

-- Obtenemos el id del tipo de medición

select @idTipoMedicion = id_medicion_biometrica
from dimensionTipoMedicionBiometrica
where descripcion = @inTipoMedicion

-- Si el registro no existe lo agregamos
if @idTipoMedicion is null

begin

insert into dimensionTipoMedicionBiometrica values (@inTipoMedicion,@inUnidad)

-- Obtenemos el id del tipo de medición

select @idTipoMedicion = id_medicion_biometrica
from dimensionTipoMedicionBiometrica
where descripcion = @inTipoMedicion

end

-- Insertamos el registro dentro de la tabla hechos biometria

insert into tabHechos_Biometria values (@idTipoMedicion, @inValorMedicion, @idPartido, @idTipoSensor,@idJugador)

go