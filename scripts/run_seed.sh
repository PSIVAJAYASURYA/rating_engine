#!/bin/bash
# scripts/run_seed.sh
# Run this to seed the MySQL database

mysql -uroot -prootpass < seed_homeowners.sql
echo "Database seeding complete!"
