FROM jupyter/minimal-notebook

USER root 
RUN apt-get update && apt-get upgrade -y && apt-get install -y gdal-bin libgdal-dev g++ poppler-utils
USER jovyan

RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install python-magic altair vincent geopandas folium sqlacodegen openpyxl simplejson treelib
# xeus-python