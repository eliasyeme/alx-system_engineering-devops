# configure ssh client to use the private key ~/.ssh/school
file_line { 'ssh_private_key':
  ensure  => present,
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

# turn off password authentication for ssh
file_line { 'disable_password_authentication':
  ensure  => present,
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  path    => '/etc/ssh/sshd_config',
  replace => true,
}
