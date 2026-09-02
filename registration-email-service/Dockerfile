# Stage 1: Build .NET application
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build

WORKDIR /src

COPY RegistrationEmailService.csproj .
RUN dotnet restore RegistrationEmailService.csproj

COPY . .

RUN dotnet publish RegistrationEmailService.csproj \
    -c Release \
    -o /app/publish \
    /p:UseAppHost=false


# Stage 2: Run .NET application
FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS runtime

WORKDIR /app

ENV ASPNETCORE_URLS=http://+:8080

COPY --from=build /app/publish .

EXPOSE 8080

ENTRYPOINT ["dotnet", "RegistrationEmailService.dll"]