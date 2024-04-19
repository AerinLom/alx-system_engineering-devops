package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
  options  => ['--no-document'], # Use '--no-document' instead of '--no-rdoc' and '--no-ri'
}

