# Seting up ssh config file using puppet
file_line { 'No passwd authentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}

file_line { 'Delare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '     IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}
