from backbone.adapter.abstract_data_model import MAPPER_REGISTRY
from product.adapters import data_models
from product.domain import entities


# from sqlalchemy.orm import mapper
def start_mappers():
    MAPPER_REGISTRY.map_imperatively(entities.categoryEntity, data_models.category_detail_data_model)
    MAPPER_REGISTRY.map_imperatively(entities.productEntity, data_models.product_data_model)
    MAPPER_REGISTRY.map_imperatively(entities.clickHistoryEntity, data_models.click_history_data_model)
    # MAPPER_REGISTRY.map_imperatively(entities.categoryEntity, data_models.user_detail_data_model)
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
