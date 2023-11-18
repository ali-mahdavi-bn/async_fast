from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from enumeration.adapters import data_models
from enumeration.domain import entities


def start_mappers():
    MAPPER_REGISTRY.map_imperatively(entities.Enumeration, data_models.enumeration_data_model)
    MAPPER_REGISTRY.map_imperatively(entities.Province, data_models.province_data_model)
    MAPPER_REGISTRY.map_imperatively(entities.City, data_models.city_data_model)

