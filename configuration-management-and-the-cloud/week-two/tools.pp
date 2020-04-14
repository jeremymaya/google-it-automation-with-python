# This example uses Puppet to make sure that htop is installed on each computer for debugging

# htop package is a tool similar to top that shows some extra information
package { 'htop':
  # ensures that the package is present on a computer
  ensure => present,
}

# Run the rules using 'sudo puppet apply -v tools.pp'
# The -v flag tells Puppet that we want to get verbose output
