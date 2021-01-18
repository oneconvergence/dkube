import kfp
from kfp.components._structures import MetadataSpec
from typing import Callable


def componentize(fn: Callable, name: str, desc: str,
                 image: str, annotations: dict, labels: dict):
    labels.update({'wfid': '{{workflow.uid}}', 'runid': '{{pod.name}}'})
    md = MetadataSpec(annotations=annotations, labels=labels)

    fn._component_human_name = name
    fn._component_description = desc

    fn._pipeline = True
    fn._executionid =  kfp.dsl.EXECUTION_ID_PLACEHOLDER
    fn._runid =  kfp.dsl.RUN_ID_PLACEHOLDER

    cfunc = kfp.components.create_component_from_func(
        fn,
        base_image=image,
    )
    cfunc.component_spec.metadata = md
    envs : Mapping[str, str] = {'pipeline': 'true', 'wfid': '{{workflow.uid}}', 'runid': '{{pod.name}}'}
    cfunc.component_spec.implementation.container.env = envs
    cfunc.component_spec.save("dkube-slurmjob-kfpl-op.yaml")
    return cfunc
