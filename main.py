
import etl.extract as extract
import etl.transform as transform
import etl.load as load
def main():
        extract.air_pollutant()
        extract.weather()
        extract.merge()

        transform.unique_id(pollutant_merge)
        transform.missing_value(pollutant_merge)
        transform.outliers(pollutant_merge)
        transform.normalization(pollutant_merge)

        load.save_transformed_csv(pollutant_merge)



        





if __name__ == "__main__":
        main()