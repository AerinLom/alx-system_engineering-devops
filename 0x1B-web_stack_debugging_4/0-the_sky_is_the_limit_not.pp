# Increases the amount of requests the server can handle successfully

exec { 'increase_ulimit_nginx':
  command => '/bin/sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -q "ULIMIT=\"-n 15\"" /etc/default/nginx',
  notify  => Exec['nginx_restart'],
}

exec { 'nginx_restart':
  command     => '/etc/init.d/nginx restart',
  path        => ['/etc/init.d'],
}
