# from mcr.microsoft.com/mssql/server:2019-latest

# env SA_PASSWORD: YourStrongPassw0rd\
#     ACCEPT_EULA: Y

# expose 1433

# copy Create_db.sql .
# copy entrypoint.sh .

# user root
# run chmod +x ./entrypoint.sh
# user mssql
# entrypoint ["./entrypoint.sh"]


FROM mcr.microsoft.com/mssql/server:2019-latest

# Set environment variables
ENV SA_PASSWORD=YourStrongPassw0rd \
    ACCEPT_EULA=Y

# Expose SQL Server port
EXPOSE 1433

# Copy SQL script and entrypoint script to the container
# COPY Create_db.sql /Create_db.sql
# COPY entrypoint.sh /entrypoint.sh

copy src/database/Create_db.sql .
copy src/database/entrypoint.sh .

# Change to root to set executable permissions on the entrypoint script
USER root
RUN chmod +x /entrypoint.sh

# Revert back to the mssql user
USER mssql

# Set the entrypoint to the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]