# Kills a process named killmenow using puppet
exec { 'pkill killmenow':
	path => '/usr/bin:/usr/sbin:/bin'
}
