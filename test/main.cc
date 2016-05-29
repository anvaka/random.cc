#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include "catch.hpp"
#include "random.cc/random.h"

TEST_CASE( "It can generate seeded random number generator", "[prng]" ) {
  Random first(42), second(42);

  REQUIRE( first.nextDouble() == second.nextDouble() );
}
