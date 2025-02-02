{#- -*- mode: sgml; tab-width: 1; indent-tabs-mode: nil -*-
 #
 # SPDX-License-Identifier: MIT
 # Copyright (c) 2022 MBition GmbH
-#}

{%- macro printEnvDataDesc(env_data_desc) %}
<ENV-DATA-DESC ID="{{env_data_desc.odx_id.local_id}}">
  <SHORT-NAME>{{env_data_desc.short_name}}</SHORT-NAME>
  <LONG-NAME>{{env_data_desc.long_name}}</LONG-NAME>
  <PARAM-SNREF SHORT-NAME="{{env_data_desc.param_snref}}"/>
  <ENV-DATA-REFS>
    {%- for env_data_ref in env_data_desc.env_data_refs %}
    <ENV-DATA-REF ID-REF="{{env_data_ref.ref_id}}"/>
    {%- endfor %}
  </ENV-DATA-REFS>
</ENV-DATA-DESC>
{%- endmacro -%}
