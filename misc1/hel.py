from pygal.maps.world import World
wm=World()
wm.force_uri_protocol='http'
wm.title="maps of central america"
wm.add('north america',{'ca':84949494949,'mx':494794164,'us':99794616})
wm.render_to_file('map.svg')
       
