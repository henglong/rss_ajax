#!/usr/bin/perl -Tw
# This is an AJAX and RSS feed page

use strict;
use LWP::UserAgent;
use XML::RSS;
use JSON;
use base qw(CGI::Ex::App);
use CGI::Ex::Dump qw(debug);

my $rss = XML::RSS->new;
my $ua = LWP::UserAgent->new;

__PACKAGE__->navigate;
exit;

sub template_path { './templates' }

sub ajax_run_step {
  my $self = shift;
  my $form = $self->{'form'};
  $self->cgix->print_content_type("application/json");
  print to_json({$self->slap_url($form->{'url'})});
  $self->{'_no_post_navigate'} = 1;
  return 1;
}

sub slap_url {
  my $self = shift;
  my $form = $self->{'form'};
  my $url = $form->{'url'};
  my $content = $ua->get($url);
  my $results = $rss->parse($content->content);
  return %$results;
}


