from store.adapters import data_models
from store.domain import entities
from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from sqlalchemy.orm import mapper
def start_mappers():
    MAPPER_REGISTRY.map_imperatively(entities.BrandEntity, data_models.brand_data_model)
    MAPPER_REGISTRY.map_imperatively(entities.StoreEntity, data_models.store_data_model)
    # read_only_mapper()
    # MAPPER_REGISTRY.map_imperatively(entities.OrganizationPersonnel, data_models.organization_personnel_table)
    # MAPPER_REGISTRY.map_imperatively(entities.OrganizationGroup, data_models.organization_group_data_model,
    #                                  properties={"members": relationship(member_mapper,
    #                                                                      primaryjoin='and_(foreign(OrganizationGroup.uuid) == OrganizationGroupMember.group_id, OrganizationGroupMember.deleted_at == None)',
    #                                                                      uselist=True)},
    #                                  exclude_properties=["members"],
    #                                  allow_partial_pks=False
    #                                  )
    #
    # MAPPER_REGISTRY.map_imperatively(OrganizationJobDTO, data_models.organization_job_table,
    #                                  properties={"role_type": relationship(role_type_mapper, lazy='joined')},
    #                                  )

# def read_only_mapper():
#     MAPPER_REGISTRY.map_imperatively(dto.OrganizationDTO, data_models.organization_data_model)
#     MAPPER_REGISTRY.map_imperatively(dto.EmployeeDTO, data_models.organization_employee_data_model, properties={
#         'personnel': relationship(dto.PersonnelDTO, viewonly=True, lazy='joined'),
#         'role': relationship(OrganizationChartNodeDto,
#                              primaryjoin='and_(foreign(EmployeeDTO.role_id) == OrganizationChartNodeDto.uuid, OrganizationChartNodeDto.deleted_at == None)',
#                              viewonly=True, lazy='joined'),
#     })
