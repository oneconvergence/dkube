import kfp.components as kfplc
from kfp.components._structures import MetadataSpec
from typing import Callable


def componentize(fn: Callable, name: str, desc: str,
                 image: str, annotations: dict, labels: dict):
    labels.update({'wfid': '{{workflow.uid}}', 'runid': '{{pod.name}}'})
    md = MetadataSpec(annotations=annotations, labels=labels)

    fn._component_human_name = name
    fn._component_description = desc

    cfunc = kfplc.create_component_from_func(
        fn,
        base_image=image,
    )
    cfunc.component_spec.metadata = md
    cfunc.component_spec.save("dkube-slurmjob-kfpl-op.yaml")
    return cfunc
