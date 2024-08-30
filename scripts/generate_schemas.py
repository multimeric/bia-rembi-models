from pathlib import Path

from bia_rembi_models.study import Study
from bia_rembi_models.sample import Biosample
from bia_rembi_models.specimen import Specimen
from bia_rembi_models.acquisition import ImageAcquisition
from bia_rembi_models.correlation import ImageCorrelation
from bia_rembi_models.analysis import ImageAnalysis
from bia_rembi_models.study_component import StudyComponent
from bia_rembi_models.rembi_study import REMBIStudy


def main():

    output_dirpath = Path("schemas")

    objects_to_write = [
        Study,
        Biosample,
        Specimen,
        ImageAcquisition,
        ImageCorrelation,
        ImageAnalysis,
        REMBIStudy,
        StudyComponent
    ]

    for obj in objects_to_write:
        output_fpath = output_dirpath/f"{obj.__name__}.json"

        with open(output_fpath, "w") as fh:
            fh.write(obj.schema_json(indent=2))


if __name__ == "__main__":
    main()
