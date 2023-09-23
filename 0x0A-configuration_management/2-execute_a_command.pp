# Executes a kill
exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
