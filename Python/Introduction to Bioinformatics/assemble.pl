#!/usr/bin/perl
#assemble.pl -- assemble overlapping fragments of strings

# input of fragments
while ($line = <DATA>) {                  # read in fragments, 1 per line
  chop($line);                            # remove trailing carriage return
  push(@fragments,$line);                 # copy each fragment into array
}
# now array @fragments contains fragments

# we need two relationships between fragments:
# (1) which fragment shares no prefix with suffix of another fragment
#     * This tells us which fragment comes first
# (2) which fragment shares longest suffix with a prefix of another
#     * This tells us which fragment follows any fragment

# First set array of prefixes to the default value "noprefixfound".
#     Later, change this default value when a prefix is found.
#     The one fragment that retains the default value must be come first.

# Then loop over pairs of fragments to determine maximal overlap.
#     This determines successor of each fragment
#     Note in passing that if a fragment has a successor then the
#         successor must have a prefix

foreach $i (@fragments) {                  # initially set prefix of each fragment
    $prefix{$i} = "noprefixfound";         # to "noprefixfound"
    }                                      # this will be overwritten when a prefix is found

#  for each pair, find longest overlap of suffix of one with prefix of the other
#         This tells us which fragment FOLLOWS any fragment

foreach $i (@fragments) {                  # loop over fragments
    $longestsuffix = "";                   # initialize longest suffix to null

    foreach $j (@fragments) {              # loop over fragment pairs
        unless ($i eq $j) {                # don't check fragment against itself
            $combine = $i . "XXX" . $j;    # concatenate fragments, with fence XXX
            $combine =~ /([\S ]{2,})XXX\1/;   #   check for repeated sequence
            if (length($1) > length($longestsuffix)) {       # keep longest overlap
                $longestsuffix = $1;       # retain longest suffix
                $successor{$i} = $j;       # record that $j follows $i
            }
        }
    }
    $prefix{$successor{$i}} = "found";     # if $j follows $i then $j must have a prefix
}
foreach (@fragments) {                     # find fragment that has no prefix; that's the start
     if ($prefix{$_} eq "noprefixfound") {$outstring = $_;}
}
$test = $outstring;                        # start with fragment without prefix
while ($successor{$test}) {                # append fragments in order
     $test = $successor{$test};            # choose next fragment
     $outstring = $outstring . "XXX" . $test;  # append to string
     $outstring =~ s/([\S ]+)XXX\1/\1/;    # remove overlapping segment
}
$outstring =~ s/\\n/\n/g;                  # change signal \n to real carriage return
print "$outstring\n";                      # print final result

__END__
the men and women merely players;\n
one man in his time
All the world's
their entrances,$\backslash $nand one man
stage,\nAnd all the men and women
They have their exits and their entrances,\n
world's a stage,\nAnd all
their entrances,\nand one man
in his time plays many parts.
merely players;\nThey have
\end{verbatim}

\vskip\baselineskip
\vskip\baselineskip
\vskip\baselineskip


\newpage
\textbf{Problem 1.7.
An alternative, concise, version
of the program to assemble overlapping fragments (see Case Study 1.2)}


\begin{verbatim}
#!/usr/bin/perl

$/ = "";
@fragments = split("\n",<DATA>);

foreach (@fragments) { $firstfragment{$_} = $_; }

foreach $i (@fragments) {
    foreach $j (@fragments) { unless ($i eq $j) {
        ($combine = $i . "XXX" . $j) =~ /([\S ]{2,})XXX\1/;
        (length($1) <= length($successor{$i})) || { $successor{$i} = $j };
    }                         }
    undef $firstfragment{$successor{$i}};
}

$test = $outstring = join "", values(%firstfragment);
while ($test = $successor{$test}) { ($outstring .= "XXX" . $test) =~ s/([\S ]+)XXX\1/\1/; }

$outstring =~ s/\\n/\n/g; print "$outstring\n";

__END__
the men and women merely players;\n
one man in his time
All the world's
their entrances,\nand one man
stage,\nAnd all the men and women
They have their exits and their entrances,\n
world's a stage,\nAnd all
their entrances,\nand one man
in his time plays many parts.
merely players;\nThey have
