# pelisalacarta.sports
Ver deportes en streaming en un canal extra dentro del plugin pelisalacarta.

- Por ahora se muestran los eventos de RojaDirecta.me y Drakulastream.eu, y se pueden ver los streamings de algunos servidores soportados.
- Se puede configurar un equipo preferido, y acceder directamente a sus links (para los días que juega tu equipo).


#### Ficheros a modificar respecto al pelisalacarta original:

Básicamente hay que modificar la configuración para incorporar un campo de texto con nuestro equipo preferido (settings.conf y settings.xml), el selector de canales principal para añadir un enlace al nuevo canal (channelselector.py) y el launcher.py para importar el código del canal.

**.kodi/addons/plugin.video.pelisalacarta/resources/settings.conf**  
Añadir la siguiente línea, cambiando Barcelona por tu equipo preferido  
```
sportsmyteam=Barcelona
```

**.kodi/addons/plugin.video.pelisalacarta/resources/settings.xml**  
Añadir la siguiente línea, dentro de `<category label="General">`  
```
    <setting id="sportsmyteam" type="text" label="Mi equipo" default="Barcelona"/>
```

**.kodi/addons/plugin.video.pelisalacarta/platformcode/xbmc/settings.xml**  
Añadir la siguiente línea, después de `<setting id="player_mode" .../>`  
```
    <setting id="sportsmyteam" type="text" label="Mi equipo" default="Barcelona"/>
```

**.kodi/addons/plugin.video.pelisalacarta/channelselector.py**  
Añadir la siguiente línea, dentro de `def getmainlist():`  
```
    itemlist.append( Item(title="Deportes" , channel="sports-main" , action="mainlist" ) )
```

**.kodi/addons/plugin.video.pelisalacarta/platformcode/xbmc/launcher.py**  
Dentro de `def run():`, detrás de:  
```
            if channel_name=="buscador":
                import pelisalacarta.buscador as channel
```
Añadir:  
```
            elif channel_name[:7]=="sports-":
                exec "import pelisalacarta.channels_sports."+channel_name[7:]+" as channel"
```

#### Carpetas a añadir respecto al pelisalacarta original:

**.kodi/addons/plugin.video.pelisalacarta/pelisalacarta/channels_sports**  
Detección de eventos deportivos en webs

**.kodi/addons/plugin.video.pelisalacarta/servers_sports**  
Detección de videos en diferentes servidores


### Pendiente:

- Maquear un poco (imágenes?, ...)
- Incorporar nuevos servidores, empezando por los que más se utilizen. Una vez identificado el servidor, partir del plugin SportsDevil, en resources/catchers, para ver como lo han resuelto ellos y trasladarlo a código python.
- Incorporar nuevos canales de otras webs que contengan enlaces de streaming ?


### Canales: 

- [x] drakulastream.eu (lshunter.tv) : Los enlaces "principales" funcionan ok. Los enlaces "other links" o links externos dependen del servidor que utilizen.
- [x] rojadirecta.me : Los enlaces dependen de servidores externos. Para partidos de la liga española, los principales parecen ser: ucaster, ustream, iguide, ezcast, ? (a completar...)
- [ ] ...


### Servidores: 

- [x] lshstream : ok
- [x] iguide : ok
- [x] tutele : ok
- [x] ustream : ok
- [x] myhdcast/liveligatv : ok
- [x] goodcast/tuttosportweb : ok
- [x] liveall, leton : ok
- [x] jjcast : ok
- [ ] ucaster/tashtv : url final teóricamente resuelta, pero falla
- [ ] ezcast : teóricamente resuelta url, pero falla
- [ ] 04stream : teóricamente resuelta url, pero pendiente comprobarlo
- [ ] ...

Dentro del canal, los servidores soportados se muestran en negrita, mientras que los demás se muestran en rojo. Pero hay que tener en cuenta que los nombres de servidores que constan en las webs no siempre se corresponden con el servidor real!

